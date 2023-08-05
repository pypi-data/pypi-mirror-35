
import pandas as pd
from cognite import _constants as constants
from cognite import config
from cognite._utils import InputError
from cognite.v05 import timeseries


class DataTransferService:
    "Create a Data Transfer Service object.\n\n    Fetch timeseries from the api.\n    "

    def __init__(self, ts_data_specs, project=None, api_key=None):
        "\n        Args:\n            ts_data_specs (list):   List of Time Series Data Specs.\n            project (str):          Project name.\n            api_key (str):          Api key.\n            cookies (dict):         Cookies.\n        "
        (config_api_key, config_project) = config.get_config_variables(api_key, project)
        if not isinstance(ts_data_specs, list):
            raise InputError("DataTransferService accepts list of dataspecs")
        self.ts_data_specs = ts_data_specs
        self.api_key = api_key or config_api_key
        self.project = project or config_project

    def get_dataframes(self):
        "Return a dictionary of dataframes indexed by label - one per data spec."
        if isinstance(self.ts_data_specs[0], dict):
            return self.__get_dataframes_by_dict()
        elif isinstance(self.ts_data_specs[0], TimeSeriesDataSpec):
            return self.__get_dataframes_by_dto()
        raise InputError("DataSpec must be a dict or TimeSeriesDataSpec object.")

    def __get_dataframes_by_dto(self):
        dataframes = {}
        for tsds in self.ts_data_specs:
            ts_list = []
            for ts in tsds.time_series:
                if isinstance(ts, dict):
                    ts_list.append(ts)
                elif isinstance(ts, TimeSeries):
                    ts_dict = dict(name=ts.name, aggregates=ts.aggregates, missingDataStrategy=ts.missing_data_strategy)
                    ts_list.append(ts_dict)
                else:
                    raise InputError("time_series parameter must be a dict or TimeSeries object")
            df = timeseries.get_datapoints_frame(ts_list, tsds.aggregates, tsds.granularity, tsds.start, tsds.end)
            df = self.__apply_missing_data_strategies(df, ts_list, tsds.missing_data_strategy)
            if dataframes.get(tsds.label) is not None:
                raise InputError("Unique labels for each dataspec must be used")
            dataframes[tsds.label] = df
        return dataframes

    def __get_dataframes_by_dict(self):
        dataframes = {}
        for data_spec in self.ts_data_specs:
            ts = data_spec[constants.TIMESERIES]
            aggregates = data_spec[constants.AGGREGATES]
            granularity = data_spec[constants.GRANULARITY]
            start = data_spec.get(constants.START)
            end = data_spec.get(constants.END)
            missing_data_strategy = data_spec.get(constants.MISSING_DATA_STRATEGY)
            label = data_spec.get(constants.LABEL, "default")
            df = timeseries.get_datapoints_frame(ts, aggregates, granularity, start, end)
            df = self.__apply_missing_data_strategies(df, ts, missing_data_strategy)
            dataframes[label] = df
        return dataframes

    def __apply_missing_data_strategies(self, df, ts_list, global_missing_data_strategy):
        "Applies missing data strategies to dataframe.\n\n        Local strategies have precedence over global strategy.\n        "
        new_df = df["timestamp"]
        for ts in ts_list:
            name = ts["name"]
            colnames = [colname for colname in df.columns.values if colname.startswith(name)]
            missing_data_strategy = ts.get("missingDataStrategy", global_missing_data_strategy)
            partial_df = df[colnames]
            if missing_data_strategy == "ffill":
                partial_df = df[colnames].fillna(method="pad")
            elif missing_data_strategy and missing_data_strategy.endswith("Interpolation"):
                method = missing_data_strategy[:(-13)].lower()
                partial_df = df[colnames].interpolate(method=method, axis=0)
            new_df = pd.concat([new_df, partial_df], axis=1)
        return new_df


class TimeSeries:
    def __init__(self, name, aggregates=None, missing_data_strategy=None):
        self.name = name
        self.aggregates = aggregates
        self.missing_data_strategy = missing_data_strategy


class TimeSeriesDataSpec:
    def __init__(
        self, time_series, aggregates, granularity, missing_data_strategy=None, start=None, end=None, label=None
    ):
        self.time_series = time_series
        self.aggregates = aggregates
        self.granularity = granularity
        self.missing_data_strategy = missing_data_strategy
        self.start = start
        self.end = end
        self.label = label or "default"
