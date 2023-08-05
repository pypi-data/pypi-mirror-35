# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
         Park Ji woo
:Date: 2018. 7. 18
"""
from copy import deepcopy
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas.core.common as com
from pandas import DataFrame
from pandas import Series
from pandas.core.index import (Index, MultiIndex)
from pandas.core.indexing import convert_to_index_sliceable

from .columns import CODE, FACTORS, RET_1, DATE, MKTCAP, HOLDING, IS_MANAGED, IS_SUSPENDED, KOSPI, BENCHMARKS, \
    DEBT_RATIO
from ..io.downloader import download_latest_korea_data

PORTFOLIO_RETURN = 'portfolio_return'

START_DATE = '2001-05-31'

QUANTILE = 'quantile'
RANK = 'rank'


class Portfolio(DataFrame):
    """

    """
    _benchmark = KOSPI
    benchmarks = None

    @property
    def _constructor(self):
        return Portfolio

    def __init__(self, data=None, index=None, columns=None, dtype=None, copy: bool = False,
                 start_date: str = START_DATE, end_date: str = None,
                 include_holding: bool = False, include_finance: bool = False,
                 include_managed: bool = False, include_suspended: bool = False):

        try:
            datetime.strptime(start_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, start_date should be YYYY-MM-DD")

        if not end_date:
            end_date = datetime.today().strftime('%Y-%m-%d')

        try:
            datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, end_date should be YYYY-MM-DD")

        if data is None:
            data, self.benchmarks = download_latest_korea_data()

            if not include_holding:
                data = data.loc[~data[HOLDING], :]

            if not include_finance:
                data = data.loc[~np.isnan(data[DEBT_RATIO]), :]

            if not include_managed:
                data = data.loc[~data[IS_MANAGED], :]

            if not include_suspended:
                data = data.loc[~data[IS_SUSPENDED], :]

            data = data.loc[(start_date <= data[DATE]) & (data[DATE] <= end_date), :]
        else:
            _, self.benchmarks = download_latest_korea_data()

        DataFrame.__init__(self=self, data=data, index=index, columns=columns, dtype=dtype, copy=copy)

    def __getitem__(self, key):
        key = com._apply_if_callable(key, self)

        # shortcut if we are an actual column
        is_mi_columns = isinstance(self.columns, MultiIndex)
        try:
            if key in self.columns and not is_mi_columns:
                self._getitem_column(key)
        except:
            pass

        # see if we can slice the rows
        indexer = convert_to_index_sliceable(self, key)
        if indexer is not None:
            return self._getitem_slice(indexer)

        if isinstance(key, (Series, np.ndarray, Index, list)):
            # either boolean or fancy integer index
            return self._getitem_array(key)
        elif isinstance(key, DataFrame):
            return self._getitem_frame(key)
        elif is_mi_columns:
            return self._getitem_multilevel(key)
        else:
            return self._getitem_column(key)

    @property
    def benchmark(self):
        return self._benchmark

    @property
    def get_benchmark(self):
        return self.benchmarks.loc[self.benchmarks[CODE] == self._benchmark, :]

    def set_benchmark(self, benchmark):
        if benchmark not in BENCHMARKS:
            raise ValueError('{} is not registered.'.format(benchmark))
        else:
            self._benchmark = benchmark

    def outcome(self, benchmark=None, weighted=False):
        if benchmark is not None:
            if benchmark not in BENCHMARKS:
                raise ValueError('{} is not registered.'.format(benchmark))

        if weighted:
            portfolio_ret_1 = self.groupby([DATE]).apply(lambda x: np.average(x[RET_1], weights=x[MKTCAP]))
        else:
            portfolio_ret_1 = self.groupby([DATE])[RET_1].mean()
        portfolio_ret_1 = portfolio_ret_1.reset_index()
        portfolio_ret_1.columns = [DATE, PORTFOLIO_RETURN]

        total_return = self._calculate_total_return(portfolio_ret_1[PORTFOLIO_RETURN])

        merged_return = pd.merge(portfolio_ret_1, self.get_benchmark, on=DATE)
        merged_return = merged_return.dropna()
        benchmark_excess_returns = merged_return[PORTFOLIO_RETURN] - merged_return[RET_1]
        information_ratio = np.average(benchmark_excess_returns) / np.std(benchmark_excess_returns)

        result = DataFrame(data={
            'total_return': [total_return],
            'information_ratio': [information_ratio],
        })

        return result

    def _calculate_total_return(self, grouped_data):
        data = grouped_data.dropna()
        total_return = self._cumulate(data).iloc[-1]
        return total_return

    def periodic_rank(self, min_rank: int, max_rank: int, factor: str = MKTCAP,
                      bottom: bool = False, drop_rank: bool = True):
        """
        Select companies which have a rank bigger than or equal to min_rank, and smaller than or equal to max_rank
        for each period.

        :param min_rank: (int) The minimum rank of selected companies.
                               The ranked_companies includes the minimum ranked company.
        :param max_rank: (int) The maximum rank of selected companies.
                               The ranked_companies includes the maximum ranked company.
        :param factor: (str) The factor used to determine rank.
        :param bottom: (bool) If bottom is True, select the companies from bottom. Or, select the companies from top.
        :param drop_rank: (bool) If drop_rank is True, delete rank column from the ranked_companies.

        :return ranked_companies: (DataFrame) Selected companies for each period by rank of the factor.
        """
        assert min_rank > 0, "min_rank should be bigger than 0."
        assert max_rank > min_rank, "max_rank should be bigger than min_rank."
        assert factor in FACTORS, "factor should be in FACTORS. Check ksif.columns.Factors, please."

        self[RANK] = self.groupby(by=[DATE])[factor].transform(
            lambda x: x.rank(ascending=bottom)
        )
        ranked_companies = deepcopy(self.loc[(self[RANK] >= min_rank) & (self[RANK] <= max_rank), :])
        ranked_companies = ranked_companies.sort_values(by=[DATE, RANK])

        del self[RANK]
        if drop_rank:
            del ranked_companies[RANK]

        return ranked_companies

    def quantile_distribution_ratio(self, factor, chunk_num=10, cumulative=True, weighted=False, only_positive=False,
                                    show_plot=False):
        if factor not in FACTORS:
            raise ValueError("The factor is not exist. Use ksif.columns, please.")

        labels = [str(x) for x in range(1, chunk_num + 1)]

        data = deepcopy(self)
        data = data.dropna(subset=[factor])
        data = data.dropna(subset=[RET_1])

        if only_positive:
            data = data.loc[data[factor] > 0, :]

        data[QUANTILE] = data.groupby(by=[DATE])[factor].transform(
            lambda x: pd.qcut(x, chunk_num, labels=labels)
        )
        data[QUANTILE] = data[QUANTILE].apply(int).apply(str)

        results = DataFrame()
        for label in labels:
            labelled_data = data.loc[data[QUANTILE] == label, :]
            if weighted:
                grouped_data = labelled_data.groupby([DATE]).apply(lambda x: np.average(x[RET_1], weights=x[MKTCAP]))
            else:
                grouped_data = labelled_data.groupby([DATE])[RET_1].mean()
            grouped_data = grouped_data.rename(label)
            grouped_data = self._cumulate(grouped_data, cumulative)
            results = pd.concat([results, grouped_data], axis=1)

        if show_plot:
            plt.figure()
            results.plot()
            plt.show()

        return results

    def show_plot(self, cumulative=True, weighted=False):
        if weighted:
            grouped_data = self.groupby([DATE]).apply(lambda x: np.average(x[RET_1], weights=x[MKTCAP]))
        else:
            grouped_data = self.groupby([DATE])[RET_1].mean()

        grouped_data = self._cumulate(grouped_data, cumulative)

        plt.figure()
        grouped_data.plot()
        plt.show()

    @staticmethod
    def _cumulate(ret, cumulative=True):
        if cumulative:
            ret = ret + 1
            ret = ret.cumprod()
            ret = ret - 1
        return ret
