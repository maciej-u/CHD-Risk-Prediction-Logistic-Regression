import pandas as pd

def handle_outliers(df, multiplier=1.5, remove=False):
    """
    Identify or remove outliers in a DataFrame using the Interquartile Range (IQR) method.

    Args:
        df (pandas.DataFrame): Input DataFrame containing numeric columns.
        multiplier (float): IQR multiplier for outlier detection. Default is 1.5.
        remove (bool): If True, remove outliers; if False, identify outliers. Default is False.

    Returns:
        pandas.DataFrame: A DataFrame containing the outliers if remove is False,
                          or a DataFrame with outliers removed if remove is True.
    """
    q1 = df.quantile(0.25)
    q3 = df.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - multiplier * iqr
    upper_bound = q3 + multiplier * iqr
    
    if remove:
        return df.clip(lower=lower_bound, upper=upper_bound, axis=1)
    else:
        return df[((df < lower_bound) | (df > upper_bound))]