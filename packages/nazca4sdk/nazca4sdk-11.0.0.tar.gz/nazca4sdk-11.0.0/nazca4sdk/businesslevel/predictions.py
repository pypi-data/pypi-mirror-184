import datetime as dat

import numpy as np
import pandas as pd
from prophet import Prophet
from pydantic import ValidationError
from sklearn.metrics import mean_squared_error

from nazca4sdk.businesslevel.__brain_connection import BrainClient
from nazca4sdk.datahandling.variable_verificator import VariableIntervalSubtractionInfo, ForecastForPrediction, \
    PredictionTool


class Forecast:
    """ Prediction class"""

    def __init__(self):
        self.prediction_brain = BrainClient()

    def forecast_prediction(self, input_data: dict, input_forecast: dict, input_tool: dict):

        """Function to determine prediction values for determined input

         Args:
             ::input_data -> dictionary with parameters::
         (
            module_name: name of module,
            variable_names: list of variable names,
            time_amount: beginning of the time range
            time_unit: 'DAY','HOUR'...
        )

            ::input_forecast -> dictionary with parameters::
        {
            forecast_time_amount: int: periods forecast: 10,50,60
            forecast_time_unit: str: frequency for forecast time: '1min', '5min'...
        }

            ::input_tool -> dictionary with parameter::
        {
            predict_tool: str: prediction tool: "prophet" or "nixtla"
        }

         Returns:
             dict: prediction parameters
         """

        try:
            data_input = dict(VariableIntervalSubtractionInfo(**input_data))
            data_forecast = dict(ForecastForPrediction(**input_forecast))
            tool = dict(PredictionTool(**input_tool))

            data = {**data_input, **data_forecast, **tool}

            response = self.prediction_brain.get_prediction(data)
            result = self.prediction_brain.parse_response(response)

            if result is None:
                return None
            return result

        except ValidationError as error:
            print(error.json())
            return None
