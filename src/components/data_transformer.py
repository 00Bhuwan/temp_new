# https://chatgpt.com/share/685804db-c2b8-8009-8f66-84c12bfe685f   --> for better understanding

import os
import sys
import numpy as np
import pandas as pd

from dataclasses import dataclass
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_columns = ['Longitude', 'Latitude', 'MaxTemp_2m',
                                 'MinTemp_2m', 'Pressure', 'Humidity_2m', 'WindSpeed_10m']
            categorical_columns = ['District']

            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )
            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('onehotencoder', OneHotEncoder(handle_unknown='ignore')),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )

            logging.info(f"Categorical columns = {categorical_columns}")
            logging.info(f"Numerical columns = {numerical_columns}")

            preprocessor = ColumnTransformer(
                [
                    ('num_pipeline', num_pipeline, numerical_columns),
                    ('cat_pipeline', cat_pipeline, categorical_columns)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initialize_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            train_df = train_df.dropna(subset=["Temp_2m"])
            test_df = test_df.dropna(subset=["Temp_2m"])

            logging.info("Read train and test completed")
            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "Temp_2m"
            numerical_columns = ['Longitude', 'Latitude', 'MaxTemp_2m',
                                 'MinTemp_2m', 'Pressure', 'Humidity_2m', 'WindSpeed_10m']

            input_feature_train_df = train_df.drop(
                columns=[target_column_name], axis=1)
            target_feature_train_df = train_df.loc[:, target_column_name]

            input_feature_test_df = test_df.drop(
                columns=[target_column_name], axis=1)
            target_feature_test_df = test_df.loc[:, target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe.")

            logging.info(
                f"input_feature_train_df shape: {input_feature_train_df.shape}")
            logging.info(
                f"target_feature_train_df shape: {target_feature_train_df.shape}")

            input_feature_train_arr = preprocessing_obj.fit_transform(
                input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(
                input_feature_test_df)

            train_arr = np.concatenate(
                [
                    input_feature_train_arr.toarray(),
                    target_feature_train_df.values.reshape(-1, 1)
                ],
                axis=1
            )
            test_arr = np.concatenate(
                [
                    input_feature_test_arr.toarray(),
                    target_feature_test_df.values.reshape(-1, 1)
                ],
                axis=1
            )

            logging.info("Saved preprocessing object.")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            logging.error(f"Error in data transformation: {e}")
            raise CustomException(e, sys)
