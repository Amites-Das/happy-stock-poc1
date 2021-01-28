import pandas as pd


def calculate_sma(df, col_name, period=10):
    """
        SMA is calculated here for the columns input
    params: df: dataframe
    params: col_name: Name of the column average to be calculated on
    params: period: period of moving average. Default value is 10

    return: df: Dataframe with new column 'SMA'
    """
    df['SMA'] = df[col_name].rolling(period).mean()
    return df
