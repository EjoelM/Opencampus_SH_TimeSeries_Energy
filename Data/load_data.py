import os

import pandas as pd

BASE_PATH = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))


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
