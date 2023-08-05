# -*- coding: UTF-8 -*-

"""
analyst.rank - 按照不同的标准对股票进行排序
====================================================================
"""

from tma.collector.aggregation import agg_market_klines


class BaseRank:
    """基类"""

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def rank(self, top=None):
        raise NotImplementedError

    @property
    def top30(self):
        return self.rank(top=30)

    @property
    def top50(self):
        return self.rank(top=50)

    @property
    def top100(self):
        return self.rank(top=100)


class WeekRank(BaseRank):
    """
    排序准则：周涨幅 * 0.5 + 周振幅 * 0.5
    """

    def __init__(self, date, refresh=False):
        """周排序

        :param date: str
            每周最后一个交易日的日期，如："2018-08-03"
        :param refresh: bool 默认值 False
            是否刷新数据
        """
        desc = "以涨幅和振幅为依据的周排序方法"
        super().__init__(name='week_top', desc=desc)
        # 参数
        self.date = date
        self.refresh = refresh
        # 数据及计算结果
        self.latest_mkls = None

    def data_prepare(self):
        """获取排序需要的数据，按照排序准则进行计算"""
        mkls = agg_market_klines(k_freq='W',
                                 refresh=self.refresh)
        latest_mkls = mkls[mkls["date"] == self.date]
        latest_mkls["change"] = latest_mkls["close"] - latest_mkls['open']
        latest_mkls["change_rate"] = latest_mkls["change"] / latest_mkls["open"]
        latest_mkls["wave"] = latest_mkls["high"] - latest_mkls['low']
        latest_mkls["wave_rate"] = latest_mkls["wave"] / latest_mkls["low"]
        latest_mkls['criterion'] = 0.5 * latest_mkls["change_rate"] + \
                                   0.5 * latest_mkls["wave_rate"]
        latest_mkls.drop(['open', 'close', 'high', 'low',
                          'volume', 'change', 'wave', ], axis=1, inplace=True)
        latest_mkls.sort_values('criterion', ascending=False, inplace=True)
        self.latest_mkls = latest_mkls.reset_index(drop=True)

    def rank(self, top=None):
        """默认的排序，即 周涨幅 * 0.5 + 周振幅 * 0.5"""
        if not self.latest_mkls:
            self.data_prepare()
        if top is None:
            top_shares = list(self.latest_mkls['code'])
        else:
            indexes = range(top)
            top_shares = list(self.latest_mkls.loc[indexes, 'code'])
        return list(enumerate(top_shares, 1))

    def rank_by_change_rate(self):
        """以周涨跌幅为依据的排序"""
        if not self.latest_mkls:
            self.data_prepare()
        wr = self.latest_mkls
        wr.sort_values('change_rate', ascending=False, inplace=True)
        wr = wr.reset_index(drop=True)
        return wr

