import os
import sys
import pandas as pd
import logging
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

from sklearn.model_selection import train_test_split
from src.components.data_transformer import DataTransformationConfig
from src.components.data_transformer import DataTransformation
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


@dataclass
class DataInjectionConfig:
    train_data_path = os.path.join('artifacts', 'train.csv')
    test_data_path = os.path.join('artifacts', 'test.csv')
    raw_data_path = os.path.join('artifacts', 'data.csv')


class DataInjection:
    def __init__(self):
        self.injection_config = DataInjectionConfig()

    def initialize_data_injection(self):
        logging.info('Enter the data injection method or component')
        try:
            df = pd.read_csv('Notebook/data/dailyclimate.csv')
            logging.info('Read the dataset as a pandas dataframe')

            os.makedirs(os.path.dirname(
                self.injection_config.train_data_path), exist_ok=True)
            df.to_csv(self.injection_config.raw_data_path,
                      index=False, header=True)

            logging.info('train test split initialized')
            half_data, _ = train_test_split(df, test_size=0.5, random_state=42)
            half_half_data, _ = train_test_split(
                df, test_size=0.5, random_state=42)
            train_set, test_set = train_test_split(
                half_half_data, test_size=0.2, random_state=42)
            train_set.to_csv(
                self.injection_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.injection_config.test_data_path,
                            index=False, header=True)
            logging.info(
                'Train test split completed and data saved to artifacts folder')

            return (
                self.injection_config.train_data_path,
                self.injection_config.test_data_path,
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataInjection()
    train_data, test_data = obj.initialize_data_injection()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initialize_data_transformation(
        train_data, test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))
