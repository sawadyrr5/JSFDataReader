#!/usr/local/bin python
# -*- coding: UTF-8 -*-
from pandas_datareader import data
from pandas_datareader.base import _BaseReader

from time import sleep
import urllib.request
import urllib.error
import pandas as pd
from pandas.errors import EmptyDataError
import datetime as dt
import numpy as np

_SLEEP_TIME = 0.5
_MAX_RETRY_COUNT = 3


class _JSFReader(_BaseReader):
    base_url = 'http://www.taisyaku.jp/search_admin/comp/'

    def __init__(self, symbols=None, start=None, end=None, **kwargs):
        super(_JSFReader, self).__init__(symbols=symbols,
                                         start=start,
                                         end=end,
                                         **kwargs)
        self.date = None

    def read(self):
        # Use _DailyBaseReader's definition
        dfs = []
        for self.date in pd.date_range(self.start, self.end, freq='D'):
            df = self._read_one_data(self.url, params=self._get_params(self.symbols))
            dfs.append(df)

        output = pd.concat(dfs)
        return output

    def _get_params(self, symbol):
        params = {
            'date': dt.datetime.strftime(self.date, '%Y%m%d')
        }
        return params

    def _read_one_data(self, url, params):
        url = self.url.format(**params)
        response = urllib.request.urlopen(url)

        try:
            result = pd.read_csv(response, encoding='Shift-JIS', skiprows=4, dtype={'コード': np.object})
        except EmptyDataError:
            result = pd.DataFrame()
        finally:
            sleep(_SLEEP_TIME)

        return result


class ShinaReader(_JSFReader):
    @property
    def url(self):
        return self.base_url + 'pcsl/shina{date}.csv'

    def _read_one_data(self, url, params):
        df = super()._read_one_data(url, params)

        if df.empty:
            return df

        df['貸借申込日'] = pd.to_datetime(df['貸借申込日'], format='%Y%m%d')
        df['決済日'] = pd.to_datetime(df['決済日'], format='%Y%m%d')
        df = df.set_index(keys=['貸借申込日', 'コード', '銘柄名'], drop=True)
        return df


class ZandakaReader(_JSFReader):
    @property
    def url(self):
        return self.base_url + 'balance/zandaka{date}.csv'

    def _read_one_data(self, url, params):
        df = super()._read_one_data(url, params)

        if df.empty:
            return df

        df['申込日'] = pd.to_datetime(df['申込日'], format='%Y/%m/%d')
        df = df.set_index(keys=['申込日', 'コード', '銘柄名'], drop=True)
        return df


class SymbolError(Exception):
    pass


def DataReader(symbols=None, data_source=None, start=None, end=None, **kwargs):
    if data_source == 'shina':
        return ShinaReader(symbols=None, start=start, end=end, **kwargs).read()
    elif data_source == 'zandaka':
        return ZandakaReader(symbols=None, start=start, end=end, **kwargs).read()
    else:
        return data.DataReader(name=symbols, data_source=data_source, start=start, end=end, **kwargs)


DataReader.__doc__ = data.DataReader.__doc__

if __name__ == '__main__':
    start_date = dt.datetime(2017, 9, 1)
    end_date = dt.datetime(2017, 9, 10)

    df = DataReader(data_source='shina', start=start_date, end=end_date)
    print(
        df.head(5)
    )

    df = DataReader(data_source='zandaka', start=start_date, end=end_date)
    print(
        df.head(5)
    )
