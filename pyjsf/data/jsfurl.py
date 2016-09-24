# -*- coding: utf-8 -*-
import pandas as pd
from datetime import datetime


class _CreateJSFUrl:
    """
    jsf.co.jpアクセス用のURLを生成する
    """
    _BASE_URL = 'http://www.taisyaku.jp/search_admin/comp/'

    def __init__(self, date_from, date_to):
        self.date_from = date_from
        self.date_to = date_to

    def urls(self):
        dates = self._date_strings(self.date_from, self.date_to)
        params = [dict(date=date) for date in dates]
        return [self._BASE_URL.format(**param) for param in params]

    @staticmethod
    def _date_strings(start, end):
        dates = [datetime.strftime(date, '%Y%m%d') for date in pd.date_range(start, end, freq='D')]
        return sorted(dates)


class CreateUrlShina(_CreateJSFUrl):
    def __init__(self, date_from, date_to):
        super().__init__(date_from, date_to)
        self._BASE_URL += 'pcsl/shina{date}.csv'


class CreateUrlZandaka(_CreateJSFUrl):
    def __init__(self, date_from, date_to):
        super().__init__(date_from, date_to)
        self._BASE_URL += 'balance/zandaka{date}.csv'
