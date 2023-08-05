import copy
from typing import Callable
from typing import cast
from typing import Dict
from typing import Iterable
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

import numpy as np
from optuna._transform import _SearchSpaceTransform
from optuna.distributions import BaseDistribution
from optuna.importance._base import BaseImportanceEvaluator
from optuna.study import Study
from optuna.trial import FrozenTrial
from optuna.trial import TrialState
from sklearn.ensemble import RandomForestRegressor

from optuna_fast_fanova._fanova import FanovaTree


class FanovaImportanceEvaluator(BaseImportanceEvaluator):
    """Cython accelerated fANOVA importance evaluator.

    Args:
        n_trees:
            The number of trees in the forest.
        max_depth:
            The maximum depth of the trees in the forest.
        seed:
            Controls the randomness of the forest. For deterministic behavior, specify a value
            other than :obj:`None`.
        completed_trials:
            Avoid to call ``study.get_trials()`` and use this value instead (default: None).
    """

    def __init__(
        self,
        *,
        n_trees: int = 64,
        max_depth: int = 64,
        seed: Optional[int] = None,
        completed_trials: Optional[List[FrozenTrial]] = None,
    ) -> None:
        self._forest = RandomForestRegressor(
            n_estimators=n_trees,
            max_depth=max_depth,
            min_samples_split=2,
            min_samples_leaf=1,
            random_state=seed,
        )
        self._completed_trials = completed_trials

    def evaluate(
        self,
        study: Study,
        params: Optional[List[str]] = None,
        *,
        target: Optional[Callable[[FrozenTrial], float]] = None,
    ) -> Dict[str, float]:
        if target is None and study._is_multi_objective():
            raise ValueError(
                "If the `study` is being used for multi-objective optimization, "
                "please specify the `target`. For example, use "
                "`target=lambda t: t.values[0]` for the first objective value."
            )

        if self._completed_trials is None:
            completed_trials = study.get_trials(deepcopy=False, states=(TrialState.COMPLETE,))
        else:
            completed_trials = self._completed_trials

        _fast_check_evaluate_args(completed_trials, params)
        if params is None:
            distributions = _fast_intersection_search_space(completed_trials)
        else:
            distributions = _fast_get_distributions(completed_trials, params)

        if len(distributions) == 0:
            return {}

        # fANOVA does not support parameter distributions with a single value.
        # However, there is no reason to calculate parameter importance in such case anyway,
        # since it will always be 0 as the parameter is constant in the objective function.
        zero_importances = {name: 0.0 for name, dist in distributions.items() if dist.single()}
        distributions = {name: dist for name, dist in distributions.items() if not dist.single()}

        trials = []
        for trial in _filter_nonfinite(completed_trials, target=target):
            if any(name not in trial.params for name in distributions.keys()):
                continue
            trials.append(trial)

        # Many (deep) copies of the search spaces are required during the tree traversal and using
        # Optuna distributions will create a bottleneck.
        # Therefore, search spaces (parameter distributions) are represented by a single
        # `numpy.ndarray`, coupled with a list of flags that indicate whether they are categorical
        # or not.
        trans = _SearchSpaceTransform(distributions, transform_log=False, transform_step=False)
        n_trials = len(trials)
        trans_params = np.empty((n_trials, trans.bounds.shape[0]), dtype=np.float64)
        trans_values = np.empty(n_trials, dtype=np.float64)

        for trial_idx, trial in enumerate(trials):
            trans_params[trial_idx] = trans.transform(trial.params)
            trans_values[trial_idx] = trial.value if target is None else target(trial)

        if trans_params.size == 0:  # `params` were given but as an empty list.
            return {}

        self._forest.fit(X=trans_params, y=trans_values)

        importances = compute_importance(self._forest, trans, distributions.keys())
        importances = {**importances, **zero_importances}
        total_importance = sum(importances.values())
        for name in importances:
            importances[name] /= total_importance

        sorted_importances = dict(
            reversed(
                sorted(
                    importances.items(),
                    key=lambda name_and_importance: name_and_importance[1],
                )
            )
        )
        return sorted_importances


def compute_importance(
    forest: RandomForestRegressor,
    transform: _SearchSpaceTransform,
    param_names: List[str],
) -> Dict[str, float]:
    search_spaces = transform.bounds
    trees = [FanovaTree(e.tree_, search_spaces) for e in forest.estimators_]

    if all(tree.variance == 0 for tree in trees):
        # If all trees have 0 variance, we cannot assess any importances.
        # This could occur if for instance `X.shape[0] == 1`.
        raise RuntimeError("Encountered zero total variance in all trees.")

    variances = np.empty(shape=(len(param_names), len(trees)), dtype=np.float64)
    importances = {}

    for i, name in enumerate(param_names):
        raw_feature = transform.column_to_encoded_columns[i]
        for tree_index, tree in enumerate(trees):
            marginal_variance = tree.get_marginal_variance(raw_feature)
            variances[i, tree_index] = np.clip(marginal_variance, 0.0, None)

        importance, _ = get_importance(trees, i, variances)
        importances[name] = importance

    return importances


def get_importance(
    trees: List[FanovaTree],
    feature: int,
    variances: np.ndarray,
) -> Tuple[float, float]:
    fractions: Union[List[float], np.ndarray] = []

    for tree_index, tree in enumerate(trees):
        tree_variance = tree.variance
        if tree_variance > 0.0:
            fraction = variances[feature, tree_index] / tree_variance
            fractions = np.append(fractions, fraction)

    fractions = np.asarray(fractions)
    return float(fractions.mean()), float(fractions.std())


def _fast_intersection_search_space(completed_trials: List[FrozenTrial]):
    search_space = None
    for trial in reversed(completed_trials):
        if search_space is None:
            search_space = trial.distributions
            continue

        delete_list = []
        for param_name, param_distribution in search_space.items():
            if param_name not in trial.distributions:
                delete_list.append(param_name)
            elif trial.distributions[param_name] != param_distribution:
                delete_list.append(param_name)

        for param_name in delete_list:
            del search_space[param_name]

    search_space = search_space or {}
    return {k: copy.copy(search_space[k]) for k in sorted(search_space)}


def _fast_check_evaluate_args(
    completed_trials: List[FrozenTrial], params: Optional[List[str]]
) -> None:
    if len(completed_trials) == 0:
        raise ValueError("Cannot evaluate parameter importances without completed trials.")
    if len(completed_trials) == 1:
        raise ValueError("Cannot evaluate parameter importances with only a single trial.")

    if params is not None:
        if not isinstance(params, (list, tuple)):
            raise TypeError(
                "Parameters must be specified as a list. Actual parameters: {}.".format(params)
            )
        if any(not isinstance(p, str) for p in params):
            raise TypeError(
                "Parameters must be specified by their names with strings. Actual parameters: "
                "{}.".format(params)
            )

        if len(params) > 0:
            at_least_one_trial = False
            for trial in completed_trials:
                if all(p in trial.distributions for p in params):
                    at_least_one_trial = True
                    break
            if not at_least_one_trial:
                raise ValueError(
                    "Study must contain completed trials with all specified parameters. "
                    "Specified parameters: {}.".format(params)
                )


def _fast_get_distributions(
    completed_trials: List[FrozenTrial], params: Optional[List[str]]
) -> Dict[str, BaseDistribution]:
    # New temporary required to pass mypy. Seems like a bug.
    params_not_none = params
    assert params_not_none is not None

    # Compute the search space based on the subset of trials containing all parameters.
    distributions = None
    for trial in completed_trials:
        trial_distributions = trial.distributions
        if not all(name in trial_distributions for name in params_not_none):
            continue

        if distributions is None:
            distributions = {
                k: trial_distributions[k] for k in trial_distributions if k in params_not_none
            }
            continue

        if any(
            trial_distributions[name] != distribution
            for name, distribution in distributions.items()
        ):
            raise ValueError(
                "Parameters importances cannot be assessed with dynamic search spaces if "
                "parameters are specified. Specified parameters: {}.".format(params)
            )

    assert distributions is not None  # Required to pass mypy.
    return {k: copy.copy(distributions[k]) for k in sorted(distributions)}


def _filter_nonfinite(
    trials: Iterable[FrozenTrial],
    target: Optional[Callable[[FrozenTrial], float]] = None,
) -> List[FrozenTrial]:
    # For multi-objective optimization target must be specified to select
    # one of objective values to filter trials by (and plot by later on).
    # This function is not raising when target is missing, sice we're
    # assuming plot args have been sanitized before.
    if target is None:

        def _target(t: FrozenTrial) -> float:
            return cast(float, t.value)

        target = _target

    filtered_trials: List[FrozenTrial] = []
    for trial in trials:
        # Not a Number, positive infinity and negative infinity are considered to be non-finite.
        if np.isfinite(target(trial)):
            filtered_trials.append(trial)
    return filtered_trials
