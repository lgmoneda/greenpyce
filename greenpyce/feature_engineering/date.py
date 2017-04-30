def time_count_between_dates(df, base_column, diff_columns, units="DMY"):
    """
    Creates a column with the difference in some time units from dates in a column and
    all other date-columns passed.

    It's assumed to be a datetime field.
    """
    import datetime

    unit_dict = {"D": 1.0,
                 "M": 30.0,
                 "Y": 365.0}
    units = [unit for unit in units]
    
    for column in diff_columns:
        delta = (df[column] - df[base_column]).apply(lambda x: x.days)
        for unit in units:
            df["diff_" + column + "_AND_" + base_column + "_" + unit] = delta / unit_dict[unit]
            
    del delta
    return df

def expand_date_info(df, columns, hour_feats=False):
    """
    Create year, month, day, hour and minute from a datetime column.
    """
    for column in columns:
        df[column + "_DAY"] = df[column].apply(lambda x: x.day)
        df[column + "_MONTH"] = df[column].apply(lambda x: x.month)
        df[column + "_YEAR"] = df[column].apply(lambda x: x.year)
        if hour_feats:
            df[column + "_HOUR"] = df[column].apply(lambda x: x.hour)

    return df

def day_of_week(df, columns):
    """
    Creates a new column with day of week information for given datetime columns.
    0: Monday
    6: Sunday
    """
    for column in columns:
        df[column + "_DAY_OF_WEEK"] = df[column].apply(lambda x: x.weekday())

    return df

def period_of_day(df, columns):
    """
    Creates a new column with period of day information for given datetime columns.
    """
    period_dict = {}
    period_dict["Morning"] = {"interval": range(6, 12), "encode": 0}
    period_dict["Afternoon"] = {"interval": range(12, 18), "encode": 1}
    period_dict["Night"] = {"interval": range(18, 24), "encode": 2}
    period_dict["Late"] = {"interval": range(0, 6), "encode": 3}

    def what_period(x):
        for key, value in period_dict.items():
            if x in value["interval"]:
                return value["encode"]
        
    for column in columns:
        df[column + "_PERIOD_OF_DAY"] = df[column].apply(lambda x: what_period(x))

    return df
