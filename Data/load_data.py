import os
from typing import Union
from darts import TimeSeries
import pandas as pd


BASE_PATH = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))

load_data_path = [
    "energy-charts_Public_net_electricity_generation_in_Germany_in_2017.csv",
    "energy-charts_Public_net_electricity_generation_in_Germany_in_2018.csv",
    "energy-charts_Public_net_electricity_generation_in_Germany_in_2019.csv",
]

air_temperature_path = [
    "energy-charts_Air_temperature_in_Germany_in_2017.csv",
    "energy-charts_Air_temperature_in_Germany_in_2018.csv",
    "energy-charts_Air_temperature_in_Germany_in_2019.csv"
]


def get_input_data(use_darts: bool = False) -> Union[pd.DataFrame, TimeSeries]:
    """
    Concatenates and processes dataframes, and optionally returns a TimeSeries object.
    Parameters:
        use_darts (bool): Whether to return a TimeSeries object using Darts library. Default is False.
    Returns:
        Union[pd.DataFrame, TimeSeries]: Concatenated and processed dataframe, or a TimeSeries object if darts_data is True.
    """
    load_df = pd.concat(
        pd.read_csv(os.path.join(BASE_PATH, load_data_path[i]), index_col=[0], skiprows=[1])
        for i in range(len(load_data_path))
    )
    temp_df = pd.concat(
        pd.read_csv(os.path.join(BASE_PATH, air_temperature_path[i]), index_col=[0], skiprows=[1])
        for i in range(len(air_temperature_path))
    )
    load_df.index = pd.to_datetime(load_df.index)
    load_df = load_df.resample('H').sum(min_count=1)
    load_df['Temperature'] = temp_df['value'].to_list()

    if use_darts:
        return TimeSeries.from_series(load_df)

    return load_df


def get_energy_data() -> pd.DataFrame:
    df = transform_consumption_data_to_hourly_data(load_consumption_data()).copy()
    df['Temperature'] = load_temperature_data()['value'].to_list()
    return df


def transform_consumption_data_to_hourly_data(df_consumption: pd.DataFrame) -> pd.DataFrame:
    df_consumption.index = pd.to_datetime(df_consumption.index)
    return df_consumption.resample('H').sum(min_count=1)


def load_consumption_data() -> pd.DataFrame:
    df_consumption_2017 = pd.read_csv(
        os.path.join(BASE_PATH, "energy-charts_Public_net_electricity_generation_in_Germany_in_2017.csv"),
        index_col=[0], skiprows=[1])
    df_consumption_2018 = pd.read_csv(
        os.path.join(BASE_PATH, "energy-charts_Public_net_electricity_generation_in_Germany_in_2018.csv"),
        index_col=[0], skiprows=[1])
    df_consumption_2019 = pd.read_csv(
        os.path.join(BASE_PATH, "energy-charts_Public_net_electricity_generation_in_Germany_in_2019.csv"),
        index_col=[0], skiprows=[1])
    return pd.concat([df_consumption_2017, df_consumption_2018, df_consumption_2019])


def load_temperature_data() -> pd.DataFrame:
    df_temperature_2017 = pd.read_csv(
        os.path.join(BASE_PATH, "energy-charts_Air_temperature_in_Germany_in_2017.csv"),
        skiprows=[1])
    df_temperature_2018 = pd.read_csv(
        os.path.join(BASE_PATH, "energy-charts_Air_temperature_in_Germany_in_2018.csv"),
        skiprows=[1])
    df_temperature_2019 = pd.read_csv(
        os.path.join(BASE_PATH, "energy-charts_Air_temperature_in_Germany_in_2019.csv"),
        skiprows=[1])
    return pd.concat([df_temperature_2017, df_temperature_2018, df_temperature_2019])
