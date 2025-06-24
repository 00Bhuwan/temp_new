import sys
import os

from dataclasses import dataclass

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info('train and test data split')
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1],
            )
            models = {"RandomForestRegressor": RandomForestRegressor()}
            # params = {
            #     "Random Forest": {
            #         # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
            #         # 'max_features':['sqrt','log2',None],
            #         'n_estimators': [8, 16, 32, 64, 128, 256]
            #     }
            # }
            model_report: dict = evaluate_models(
                X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models)
            best_model_score = max(model_report.values())
            best_model_name = list(model_report.keys())[list(
                model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]
            if best_model_score < 0.6:
                raise CustomException('No best model found')
            logging.info(f"Best model found: {best_model_name}")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)
            final_r2 = r2_score(y_test, predicted)

            return final_r2

        except Exception as e:
            logging.info(f"Error in model: {e}")
            raise CustomException(e, sys)
