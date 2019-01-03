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

    def populate_first_female(self):
        filename = './data/names/dist.female.first'

        # use pandas to get data
        df_first = pd.read_csv(filename, sep=' ')
        series = df_first.iloc[:, 0]
        series.dropna(inplace=True)

        # convert pandas series to set, store in instance variable
        self.first_female = set(series)


if __name__ == "__main__":

    names = Names()
    names.populate_first_female()
    print(names.first_female)

    if 'Kathy'.upper() in names.first_female:
        print('found Kathy')
