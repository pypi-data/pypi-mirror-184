"""@Author Rayane AMROUCHE

Model Class
"""

from typing import Any, Callable

import optuna  # type: ignore

from dsmanager.datamanager.datastorage import DataStorage
from dsmanager.controller.utils import fill_kwargs


class Model():
    """Estimor Class to parametrize model in a pipeline
    """

    def __init__(
            self,
            estimator: Any,
            objective: Callable[[Any, Any, Any, Any], Any],
            scoring: Any = None,
            direction: Any = None,
    ) -> None:
        """Init class Model with an estimator

        Args:
            estimator (Any): Estimator associated
            objective (Any): objective function
            scoring (Any, optional)): scoring function. Defaults to None.
            direction (Any, optional)): direction of the objective. Defaults to
                None.
        """
        def fed_objective(trial: Any,
                          x_data: Any,
                          y_data: Any,
                          spliting: Any) -> Any:
            args = [
                trial,
                estimator,
                x_data,
                y_data,
                spliting,
                scoring,
            ]
            return objective(*args)
        self.objective = fed_objective
        self.__estimator = estimator
        self.__direction = direction
        self.__estimator_instance = None
        self.studies = DataStorage()

    def fit(self,
            X: Any,  # pylint: disable=invalid-name
            y: Any = None,  # pylint: disable=invalid-name
            reload: bool = False,
            **kwargs: Any) -> None:
        """Fit the model according to the given training data

        Args:
            X (Any): Training data matrix
            y (Any, optional): Target vector. Defaults to None.
            reload (bool, optional): If true, instance is reseted to None.
                Defaults to None.
        """
        estimator_kwargs = fill_kwargs(self.__estimator, **kwargs)
        if reload or self.__estimator_instance is None:
            self.__estimator_instance = self.__estimator(**estimator_kwargs)
        if self.__estimator_instance is not None:
            fit_kwargs = fill_kwargs(self.__estimator_instance.fit, **kwargs)
            self.__estimator_instance.fit(X, y, **fit_kwargs)

    def predict(self,
                X: Any,  # pylint: disable=invalid-name
                ) -> None:
        """Predict class labels for samples in X

        Args:
            X (Any): The data matrix for which we want to get the predictions

        Raises:
            Exception: Raised if model is not fitted

        Returns:
            Any: Vector containing the class labels for each sample.
        """
        if self.__estimator_instance is None:
            raise Exception("The model is not fitted")
        return self.__estimator_instance.predict(X)

    def predict_proba(self,
                      X: Any,  # pylint: disable=invalid-name
                      ) -> None:
        """Probability estimates.

        Args:
            X (Any): The data matrix for which we want to get the predictions

        Raises:
            Exception: Raised if model is not fitted

        Returns:
            Any: Returns the probability of the sample for each class in the
                model
        """
        if self.__estimator_instance is None:
            raise Exception("The model is not fitted")
        return self.__estimator_instance.predict_proba(X)

    def score(self,
              X: Any,  # pylint: disable=invalid-name
              y: Any = None) -> Any:  # pylint: disable=invalid-name
        """Score using the `scoring` option on the given test data and labels

        Args:
            X (Any): The data matrix for which we want to get the predictions
            y (Any, optional): True labels for X. Defaults to None.

        Raises:
            Exception: Raised if model is not fitted

        Returns:
            Any: Score of self.predict(X) wrt. y.
        """
        if self.__estimator_instance is None:
            raise Exception("The model is not fitted")
        return self.__estimator_instance.score(X, y)

    def reset_instance(self) -> None:
        """Reset estimator instance to None
        """
        self.__estimator_instance = None

    def study(self,
              X: Any,  # pylint: disable=invalid-name
              y: Any,  # pylint: disable=invalid-name
              spliting: Any,
              **kwargs: Any) -> Any:  # pylint: disable=invalid-name
        """Optimize model and return a study

        Args:
            X (Any): Training data matrix
            y (Any, optional): Target vector. Defaults to None.
            spliting (Any): Spliting rule for the data

        Returns:
            Any: Study
        """
        study_params = fill_kwargs(optuna.study.create_study, **kwargs)
        optimize_params = fill_kwargs(optuna.Study.optimize, **kwargs)

        if "callbacks" not in kwargs:
            kwargs["callbacks"] = []

        def callback(study, trial):
            if study.best_trial.number == trial.number:
                if "best_model" in trial.user_attrs:
                    study.set_user_attr(
                        key="best_model",
                        value=trial.user_attrs["best_model"]
                    )
                if "best_params" in trial.user_attrs:
                    study.set_user_attr(
                        key="best_params",
                        value=trial.user_attrs["best_params"]
                    )

        kwargs["callbacks"].append(callback)

        def fed_objective(trial: Any):
            return self.objective(trial, X, y, spliting)

        study = optuna.create_study(
            **study_params,
            direction=self.__direction
        )
        study.optimize(
            fed_objective,
            **optimize_params
        )

        self.studies[study.study_name] = study
        return study
