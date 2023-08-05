import numpy as np
import pandas as pd
from scipy.stats import norm

from rdt.transformers.BaseTransformer import BaseTransformer
from rdt.transformers.NullTransformer import NullTransformer


class CatTransformer(BaseTransformer):
    """
    This class represents the categorical transformer for SDV
    """

    def __init__(self, *args, **kwargs):
        """ initialize transformer """
        super().__init__(type='categorical', *args, **kwargs)
        self.probability_map = {}  # val -> ((a,b), mean, std)

    def fit_transform(self, col, col_meta, missing=True):
        """ Returns a tuple (transformed_table, new_table_meta) """
        out = pd.DataFrame()
        col_name = col_meta['name']
        self.get_probability_map(col)
        out[col_name] = col.apply(self.get_val)
        # Handle missing

        if missing:
            nt = NullTransformer()
            res = nt.fit_transform(out, col_meta)
            return res

        return out

    def reverse_transform(self, col, col_meta, missing=True):
        """ Converts data back into original format """
        output = pd.DataFrame()
        col_name = col_meta['name']
        fn = self.get_reverse_cat(col)

        if missing:
            new_col = col.apply(fn, axis=1)
            new_col = new_col.rename(col_name)
            data = pd.concat([new_col, col['?' + col_name]], axis=1)
            nt = NullTransformer()
            output[col_name] = nt.reverse_transform(data, col_meta)

        else:
            data = col.to_frame()
            output[col_name] = data.apply(fn, axis=1)

        return output

    def get_val(self, x):
        """ Converts cat value into num between 0 and 1 """
        interval, mean, std = self.probability_map[x]
        new_val = norm.rvs(mean, std)
        return new_val

    def get_reverse_cat(self, col):
        '''Returns a converter that takes in a value and turns
        it back into a category
        '''

        def reverse_cat(x):
            res = None

            for val in self.probability_map:
                interval = self.probability_map[val][0]
                if x[0] >= interval[0] and x[0] < interval[1]:
                    res = val
                    return res

            if res is None:
                return list(self.probability_map.keys())[0]

        return reverse_cat

    def get_probability_map(self, col):
        """ Maps each unique value to probability of seeing it """
        # According to pandas docs, nan values are excluded on groupby:
        # http://pandas.pydata.org/pandas-docs/stable/missing_data.html#na-values-in-groupby
        # So we are replacing them with -1 and replace them back with np.nan after groupby
        # Further discussion: https://github.com/pandas-dev/pandas/issues/3729

        column = col.fillna(-1)
        self.probability_map = column.groupby(column).count().rename({-1: np.nan}).to_dict()
        # next set probability ranges on interval [0,1]
        cur = 0
        num_vals = len(col)
        for val in self.probability_map:
            prob = self.probability_map[val] / num_vals
            interval = (cur, cur + prob)
            cur = cur + prob
            mean = np.mean(interval)
            std = (interval[1] - interval[0]) / 6
            self.probability_map[val] = (interval, mean, std)
