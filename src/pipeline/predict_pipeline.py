import sys
import os
import pandas as pd
import logging
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = 'artifacts/model.pkl'
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            logging.info('before loading')
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            logging.info('after loading')
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 Longitude: float,
                 Latitude: float,
                 MaxTemp_2m: float,
                 MinTemp_2m: float,
                 Pressure: float,
                 Humidity_2m: float,
                 WindSpeed_10m: float,
                 District: str
                 ):
        self.Longitude = Longitude
        self.Latitude = Latitude
        self.MaxTemp_2m = MaxTemp_2m
        self.MinTemp_2m = MinTemp_2m
        self.Pressure = Pressure
        self.Humidity_2m = Humidity_2m
        self.WindSpeed_10m = WindSpeed_10m
        self.District = District

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Longitude": [self.Longitude],
                "Latitude": [self.Latitude],
                "MaxTemp_2m": [self.MaxTemp_2m],
                "MinTemp_2m": [self.MinTemp_2m],
                "Pressure": [self.Pressure],
                "Humidity_2m": [self.Humidity_2m],
                "WindSpeed_10m": [self.WindSpeed_10m],
                "District": [self.District],
            }
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
