#!/usr/bin/env python3

import pandas as pd


class Names:

    # could store names in a set, sorted list, or a list.
    # set appears best as long as it fits in memory.
    # search a (hashed?) set is fastest, ~ O(1)
    # search a sorted list using bisect is O(log(n))
    # search an unsorted list is slowest, O(n/2) ~ O(n). Don't use unsorted list.
    # https://stackoverflow.com/questions/7571635/fastest-way-to-check-if-a-value-exist-in-a-list
    # alternatively could search a pandas dataframe or series
    first_female = {}
    last_2010 = {}

    def populate_names(self):
        """
        populates instance variables like first_female and last
        for efficient access.
        """
        self.first_female = Names.get_first_female_names()
        self.last_2010 = Names.get_last_names_2010()

    @staticmethod
    def get_first_female_names():
        """
        reads data file containing first female names
        :return: set containing names
        """
        filename = './data/names/dist.female.first'

        # use pandas to get data
        df = pd.read_csv(filename, sep=' ', header=None)
        series = df.iloc[:, 0]
        series.dropna(inplace=True)

        # convert pandas series to set
        return set(series)

    @staticmethod
    def get_last_names_2010():
        """
        reads data file containing last names
        :return: set containing names
        """
        filename = './data/names/Names_2010Census_Top1000.csv'

        # use pandas to get data
        # https://stackoverflow.com/questions/42138966/pandas-read-csv-ignore-commas-one-column-per-line
        df_last = pd.read_csv(filename, sep=',', header=None)
        # df_last = pd.read_csv(filename)
        series_last = df_last.iloc[:, 0]
        series_last.dropna(inplace=True)
        series_last = series_last.str.strip()

        # convert pandas series to set, store in instance variable
        return set(series_last)


if __name__ == "__main__":

    names = Names()
    names.populate_names()
    print(names.first_female)
    print(names.last_2010)

    if 'Kathy'.upper() in names.first_female:
        print('found Kathy')
    if 'smith'.upper() in names.last_2010:
        print('found smith')
    if 'sims'.upper() in names.last_2010:
        print('found sims')
