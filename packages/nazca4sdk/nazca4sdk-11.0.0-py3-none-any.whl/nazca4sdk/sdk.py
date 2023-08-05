"""SDK to communicate with Nazca4.0 system """

from datetime import datetime
from pydantic import ValidationError

from nazca4sdk import UserVariable
from nazca4sdk.businesslevel.predictions import Forecast
from nazca4sdk.cache import Cache
from nazca4sdk.datahandling.cache.cache_storage import CacheStorage
from nazca4sdk.datahandling.cache.key_value import KeyValue
from nazca4sdk.datahandling.hotstorage.hot_storage import HotStorage
from nazca4sdk.datahandling.knowledge.knowledge_data_type import KnowledgeDataType
from nazca4sdk.datahandling.knowledge.knowledge_storage import KnowledgeStorage
from nazca4sdk.datahandling.nazcavariables.nazca_variables_storage import NazcaVariablesStorage
from nazca4sdk.datahandling.variable_verificator import VariableIntervalInfo, \
    VariableIntervalSubtractionInfo, VariableForPrediction, PredictionTool
from nazca4sdk.tools.time import get_time_delta
from nazca4sdk.businesslevel import predictions
from nazca4sdk.datahandling.hotstorage.user_variable_info import UserVariableInfo
from nazca4sdk.datahandling.variable_historical_info import VariableHistoricalInfo


class SDK:
    """SDK for Nazca4 system"""

    def __init__(self, https: bool = True):
        """ Initializing the system, checking connection and caching system configuration
        if https is required then https = True"""

        self._https = https
        self._system_cache = Cache(https)
        self._cache = CacheStorage(https)
        self._knowledge = KnowledgeStorage(https)
        self._hot_storage = HotStorage(https)
        self._nazca_variables_storage = NazcaVariablesStorage(https)
        if not self._system_cache.load:
            print("Init SDK failed")
            self.modules = []
            self.variables = []
            self.types = []
        else:
            self.modules = self._system_cache.modules
            self.variables = self._system_cache.variables

    def variable_over_day(self, module_name, variable_names, start_date, end_date):
        """Get variables in specific time range

        Args:
            module_name: name of module,
            variable_names: list of variable names,
            start_date: start time of data acquisition
            end_date: end time of data acquisition

        Returns:
            DataFrame: Variable values from selected time range

        Example:
            sdk.variable_over_day('Module_Name', ['Variable1'],
                start_date = '2000-01-01T00:00:00',
                 end_date = '2000-01-01T12:00:00')
        """
        try:
            data = {'module_name': module_name,
                    'variable_names': variable_names,
                    'start_date': start_date,
                    'end_date': end_date}
            variable_info = VariableIntervalInfo(**data)
            result = self._system_cache.variable_over_day(variable_info.module_name,
                                                          variable_info.variable_names,
                                                          variable_info.start_date,
                                                          variable_info.end_date)
            if result is None:
                return None
            return result.to_df()
        except ValidationError as error:
            print(error.json())
            return None

    def read_historical_variable(self, module_name: str,
                                 variable_names: list,
                                 start_date: str,
                                 end_date: str,
                                 page_size: int = 10000):
        """Get paged variables in specific time range

                Args:
                    module_name: name of module,
                    variable_names: list of variable names,
                    start_date: start time of data acquisition
                    end_date: end time of data acquisition
                    page_size: page size

                Returns:
                    array of variable values : Paged Variable values from selected time range

                Example:
                    sdk.read_historical_variable('Module_Name', ['Variable1'],
                         start_date = '2000-01-01T00:00:00',
                         end_date = '2000-01-01T12:00:00',
                         page_size= 100)
                """

        try:
            data = {'module_name': module_name,
                    'variable_names': variable_names,
                    'start_date': start_date,
                    'end_date': end_date,
                    'page_size': page_size}
            variable_info = VariableHistoricalInfo(**data)
            result = self._system_cache.read_historical_variable(variable_info)
            if result is None:
                return None
            return result
        except ValidationError as error:
            print(error.json())
            return None

    def variable_over_time(self, module_name: str,
                           variable_names: list,
                           time_amount: int,
                           time_unit: str):
        """ Get variables in specific time range

        Args:
            module_name: name of module,
            variable_names: list of variable names,
            time_amount: beginning of the time range
            time_unit: 'DAY','HOUR'...

        Returns:
            DataFrame: Variable values from selected time range

        Example:
              sdk.variable_over_time('Module_Name', ['Variable1'], 10, 'MINUTE')
        """
        try:
            data = {'module_name': module_name,
                    'variable_names': variable_names,
                    'time_amount': time_amount,
                    'time_unit': time_unit}
            variable_info = VariableIntervalSubtractionInfo(**data)

            end_date = datetime.now()
            start_date = end_date - get_time_delta(time_unit, time_amount)

            result = self._system_cache.variable_over_day(variable_info.module_name,
                                                          variable_info.variable_names,
                                                          start_date,
                                                          end_date)
            if result is None:
                return None
            return result.to_df()
        except ValidationError as error:
            print(error.json())
            return None

    def write_hotstorage_variables(self, user_variables: [UserVariable]):
        """
         Save user variables in hot storage
        Args:
            user_variables: list of user variables to save

        Returns:
            True - variables to save send to hot storage
            False - communication with hot storage error
        """
        return self._hot_storage.save_variables(user_variables)

    def read_hotstorage_variables(self, start_date: str, end_date: str, variables: [UserVariableInfo]):
        """Read user variables from hot storage

        Args:
            start_date: begin of time range
            end_date: end of time range
            variables: list of user variables to read

        Returns:
            list of user variables values from hot storage
        """
        return self._hot_storage.read_variables(start_date, end_date, variables)

    def read_cache_keys(self, keys):
        """
        Read cache values for list of keys

        Args:
            keys: List of keys to read from cache

        Returns:
            List of CacheEntry
        """
        return self._cache.read_keys(keys)

    def write_cache_keys(self, key: str, value):
        """write key value to cache

        Args:
            key: key
            value: value to write to cache
        Returns:
            CacheEntry if success or None if error
        """

        data = {'key': key,
                'value': value}
        try:
            variable_info = KeyValue(**data)
            return self._cache.write_keys(variable_info)
        except ValidationError as error:
            print(error.json())
            return None

    def read_knowledge(self, key: str):
        """ read knowledge for key
        Args:
            key: key 
        Returns:
            Knowledge
        """
        return self._knowledge.read_key_values(key)

    def write_knowledge(self, key: str, section: str, value: str, datatype: KnowledgeDataType):
        """Write value to knowledge

        Args:
            key: key
            section: section name
            value: value
            datatype: data type to write

            Returns:
                True - write success
                False - write error
        """
        return self._knowledge.write_key_values(key, section, value, datatype)

    def daily_media_usage(self, module_name: str, variable_name: str):
        """ Function to calculate daily media usage like air, etc.

        Args:
            module_name: name of module,
            variable_name:  desired variable,

            Returns:
                Float: Value

            Example:
                daily_media_usage('Module_Name', 'Variable_Name')
        """

        start_date = datetime.today().strftime("%Y-%m-%dT00:00:00")
        end_date = datetime.today().strftime("%Y-%m-%dT%H:%M:%S")
        try:
            data = self.variable_over_day(module_name, [variable_name], start_date=start_date, end_date=end_date)
            if data is None:
                return None
            return round(data.value.iloc[-1] - data.value.iloc[0], 2)
        except ValidationError as error:
            print(error.json())
            return None

    def daily_energy_usage(self, module_name):
        """ Function to calculate daily electric energy usage

        Args:
            module_name:  name of module,

            Returns:
                Float: Value

            Example:
                daily_energy_usage('Module_Name')
        """

        start_date = datetime.today().strftime("%Y-%m-%dT00:00:00")
        end_date = datetime.today().strftime("%Y-%m-%dT%H:%M:%S")

        try:
            ea_dec = self.variable_over_day(module_name, ['Ea_dec'], start_date=start_date, end_date=end_date)
            ea_res = self.variable_over_day(module_name, ['Ea_res'], start_date=start_date, end_date=end_date)
            if (ea_dec is None) or (ea_res is None):
                return None
            energy_now = ea_dec.value.iloc[-1] + ea_res.value.iloc[-1]
            energy_previous = ea_dec.value.iloc[0] + ea_res.value.iloc[0]
            return round(energy_now - energy_previous, 2)
        except ValidationError as error:
            print(error.json())
            return None

    def read_nazca_variables(self):
        """  Read all nazca variables

        Returns:
            all nazca variables
        """
        return self._nazca_variables_storage.read_variables()

    def read_nazca_variable(self, identifier: str):
        """ Read nazca variable with identifier
        
        Args: 
            identifier: nazca variable identifier 
        Returns: 
            nazca variable
        """
        return self._nazca_variables_storage.read_variable(identifier)

    def read_variables_stats(self, module: str, variables: [str], start_date: str, end_date: str):
        """ Read module variable stats

        Args:
            module: module name
            variables: list of variable names
            start_date: start of date range
            end_date: end of date range
        Returns:
            VariableStats list
        """
        return self._system_cache.read_variables_stats(module=module, variables=variables,
                                                       start_date=start_date,
                                                       end_date=end_date)

    def read_user_variables_stats(self, variables: [UserVariableInfo], start_date: str, end_date: str):
        """Read user variables stats

        Args:
            variables: list of variables names
            start_date: start of date range
            end_date: end of date range
        Returns:
            VariableStats list
        """

        return self._hot_storage.read_user_variables_stats(variables=variables,
                                                           start_date=start_date,
                                                           end_date=end_date)

    def predict(self, module_name: str, variable_names: list, time_amount: int, time_unit: str,
                forecast_time_amount: int, forecast_unit: str, prediction_tool: str = "prophet"):

        """
        Predict value for the future based on prophet procedure

        Args:

            module_name: name of module,
            variable_names: list of variable names,
            time_amount: beginning of the time range
            time_unit: 'DAY','HOUR'...
            forecast_time_amount: int: periods forecast: 10,50,60
            forecast_unit: str: frequency for forecast time: '1min', '5min'...
            prediction_tool: str: "prophet" or "nixtla"

        Returns:
            result dict with:
                 lower_bound, upper_bound, prediction value, mse error, mae errors
        """

        try:

            variable_data = {'variable_names': variable_names}
            variable = VariableForPrediction(**variable_data).variable_names_verify_number(variable_names)

            data = {"module_name": module_name,
                    "variable_names": variable,
                    "time_amount": time_amount,
                    "time_unit": time_unit
                    }
            forecast_data = {
                "forecast_time_amount": forecast_time_amount,
                "forecast_time_unit": forecast_unit
            }

            prediction_tool = {"prediction_tool": prediction_tool}

            prediction = Forecast()
            result = prediction.forecast_prediction(data, forecast_data, prediction_tool)
            if result is None:
                return None
            return result

        except ValidationError as error:
            print(error.json())
            return None
