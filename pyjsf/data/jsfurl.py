# -*- coding: utf-8 -*-
import pandas as pd
from datetime import datetime


class CreateJSFUrl:
    """
    jsf.co.jpアクセス用のURLを生成する
    """
    _URL = 'http://www.jsf.co.jp/de/stock/dlcsv.php?target={target}&date={date}'

    def __init__(self, date_from, date_to):
        self.date_from = date_from
        self.date_to = date_to

    def urls(self, target):
        dates = self._date_strings(self.date_from, self.date_to)
        params = [dict(target=target, date=date) for date in dates]
        return [self._URL.format(**param) for param in params]

    @staticmethod
    def _date_strings(start, end):
        dates = [datetime.strftime(date, '%Y-%m-%d') for date in pd.date_range(start, end, freq='D')]
        return sorted(dates)
