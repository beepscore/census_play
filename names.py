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
    last = {}

    def populate_first_female(self):
        filename = './data/names/dist.female.first'

        # use pandas to get data
        df = pd.read_csv(filename, sep=' ')
        series = df.iloc[:, 0]
        series.dropna(inplace=True)

        # convert pandas series to set, store in instance variable
        self.first_female = set(series)

    def populate_last(self):
        filename = './data/names/Names_2010Census_Top1000.csv'

        # use pandas to get data
        df = pd.read_csv(filename)
        series = df.iloc[:, 0]
        series.dropna(inplace=True)

        # convert pandas series to set, store in instance variable
        self.last = set(series)


if __name__ == "__main__":

    names = Names()
    names.populate_first_female()
    print(names.first_female)
    names.populate_last()
    print(names.last)

    if 'Kathy'.upper() in names.first_female:
        print('found Kathy')
    if 'little'.upper() in names.last:
        print('found little')
