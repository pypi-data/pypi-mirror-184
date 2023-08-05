"""@Author Rayane AMROUCHE

ModelManager Class
"""

import os

from typing import Any

import optuna

from dsmanager.datamanager.datastorage import DataStorage
from dsmanager.model.model import Model
from dsmanager.model.utils import Utils
from dsmanager.controller.logger import make_logger


class ModelManager:
    """ModelManager class handle all the Model work"""

    def __init__(self,
                 logger_path: str = "/tmp/logs",
                 verbose: int = 0) -> None:
        """Init Modelmanager

        Args:
            models (dict, optional): _description_. Defaults to None.
            logger_path (str, optional): _description_. Defaults to "/tmp/logs".
            verbose (int, optional): _description_. Defaults to 0.
        """
        self.models = DataStorage()
        self.logger = make_logger(
            os.path.join(logger_path, "model"),
            "modelmanager",
            verbose=verbose,
            logger=optuna.logging._get_library_root_logger()
        )
        self.utils = Utils(self, logger_path, verbose)
        self.models = DataStorage()

    def add_model(self,  # pylint: disable=too-many-arguments
                  name: str,
                  estimator: Any,
                  scoring: Any = None,
                  objective: Any = None,
                  direction: Any = None,
                  ) -> None:
        """Generate and add a model to the model manager models dict

        Args:
            name (str): Name of the model to add
            model (Any): Model class
            scoring (Any, optional): Scoring function. Defaults to None.
            objective (Any, optional): Objective function or parameters to
                generate a standard objective function. Defaults to None.
        """
        if objective is None:
            objective = self.utils.generate_objective({})
        if not callable(objective):
            objective = self.utils.generate_objective(objective)
        self.models[name] = Model(estimator, objective, scoring, direction)

    def get_model(self, name: str) -> Any:
        """Get a model from the model manager models dict

        Args:
            name (str): Name of the model

        Returns:
            Any: Model instance
        """
        return self.models[name]

    def fit(self,
            name: str,
            X: Any,  # pylint: disable=invalid-name
            y: Any = None,  # pylint: disable=invalid-name
            reload: bool = False,
            **kwargs: Any) -> None:
        """Fit the model according to the given training data

        Args:
            name (str): Name of the model to fit
            X (Any): Training data matrix
            y (Any, optional): Target vector. Defaults to None.
            reload (bool, optional): If true, instance is reseted to None.
                Defaults to None.
        """
        model = self.get_model(name)
        model.fit(X=X, y=y, reload=reload, **kwargs)

    def predict(self,
                name: str,
                X: Any,  # pylint: disable=invalid-name
                ) -> None:
        """Predict class labels for samples in X

        Args:
            name (str): Name of the model to predict
            X (Any): The data matrix for which we want to get the predictions

        Raises:
            Exception: Raised if model is not fitted

        Returns:
            Any: Vector containing the class labels for each sample.
        """
        model = self.get_model(name)
        return model.predict(X=X)

    def predict_proba(self,
                      name: str,
                      X: Any,  # pylint: disable=invalid-name
                      ) -> None:
        """Probability estimates.

        Args:
            name (str): Name of the model to predict proba
            X (Any): The data matrix for which we want to get the predictions

        Raises:
            Exception: Raised if model is not fitted

        Returns:
            Any: Returns the probability of the sample for each class in the
                model
        """
        model = self.get_model(name)
        return model.predict_proba(X=X)

    def score(self,
              name: str,
              X: Any,  # pylint: disable=invalid-name
              y: Any = None) -> Any:  # pylint: disable=invalid-name
        """Score using the `scoring` option on the given test data and labels

        Args:
            name (str): Name of the model to score
            X (Any): The data matrix for which we want to get the predictions
            y (Any, optional): True labels for X. Defaults to None.

        Raises:
            Exception: Raised if model is not fitted

        Returns:
            Any: Score of self.predict(X) wrt. y.
        """
        model = self.get_model(name)
        return model.score(X=X, y=y)

    def reset_instance(self, name: str) -> None:
        """Reset estimator instance to None

        Args:
            name (str): Name of the model to reset
        """
        model = self.get_model(name)
        model.reset_instance()

    def study(self,
              name: str,
              X: Any,  # pylint: disable=invalid-name
              y: Any,  # pylint: disable=invalid-name
              spliting: Any,
              **kwargs: Any) -> Any:  # pylint: disable=invalid-name
        """Optimize model and return a study

        Args:
            name (str): Name of the model to reset
            X (Any): Training data matrix
            y (Any, optional): Target vector. Defaults to None.
            spliting (Any): Spliting rule for the data

        Returns:
            Any: Study
        """
        model = self.get_model(name)
        return model.study(X=X, y=y, spliting=spliting, **kwargs)
