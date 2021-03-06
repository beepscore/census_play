#!/usr/bin/env python3

import pandas as pd


"""
could store names in a set, sorted list, or a list.
set appears best as long as it fits in memory.
search a (hashed?) set is fastest, ~ O(1)
search a sorted list using bisect is O(log(n))
search an unsorted list is slowest, O(n/2) ~ O(n). Don't use unsorted list.
https://stackoverflow.com/questions/7571635/fastest-way-to-check-if-a-value-exist-in-a-list
alternatively could search a pandas dataframe or series
"""


def get_first_female_names():
    """
    reads data file containing first female names
    :return: set containing first female names
    """
    filename = './data/names/dist.female.first'

    # use pandas to get data
    df = pd.read_csv(filename, sep=' ', header=None)
    series = df.iloc[:, 0]
    series.dropna(inplace=True)

    # convert pandas series to set
    return set(series)


def get_last_names_1990():
    """
    reads data file containing last names from 1990 census
    :return: set containing last names
    """
    filename = './data/names/dist.all.last'

    # use pandas to get data
    # https://stackoverflow.com/questions/42138966/pandas-read-csv-ignore-commas-one-column-per-line
    df = pd.read_csv(filename, sep=',', header=None)
    series = df.iloc[:, 0]
    series.dropna(inplace=True)
    # df_last = pd.read_csv(filename)
    series = series.str.strip()

    # convert pandas series to set
    return set(series)


def get_last_names_2010():
    """
    reads data file containing last names from 2010 census
    :return: set containing last names
    """
    filename = './data/names/Names_2010Census_Top1000.csv'

    # use pandas to get data
    # https://stackoverflow.com/questions/42138966/pandas-read-csv-ignore-commas-one-column-per-line
    df_last = pd.read_csv(filename, sep=',', header=None)
    # df_last = pd.read_csv(filename)
    series_last = df_last.iloc[:, 0]
    series_last.dropna(inplace=True)
    series_last = series_last.str.strip()

    # convert pandas series to set
    return set(series_last)


if __name__ == "__main__":

    pass
