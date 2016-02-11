#! /usr/bin/env python
# -*- coding: utf-8 -*-
# python 3.5
import urllib.request
import pandas as pd


class PyJSF:
    """
    Pythonで日本証券金融の品貸料、信用残高を取得するクラス
    """
    def __init__(self, date):
        date = pd.to_datetime(date)
        k = ['y', 'm', 'd']
        v = [str(v).zfill(2) for v in [date.year, date.month, date.day]]
        self.args = dict(zip(k, v))

    def __fetch(self, target):
        self.args['target'] = target
        url = 'http://www.jsf.co.jp/de/stock/dlcsv.php?target={target}&date={y}-{m}-{d}'.format(**self.args)
        response = urllib.request.urlopen(url)
        try:
            df = pd.read_csv(response, encoding='Shift_JIS', skiprows=3)
        except(pd.parser.CParserError):
            df = pd.DataFrame()
        return df

    def shina(self):
        return self.__fetch('pcsl')

    def balance(self):
        return self.__fetch('balance')

if __name__ == '__main__':
    myJSF = PyJSF('2016-02-09')
    print(myJSF.shina())    # 品貸料率取得
    print(myJSF.balance())  # 信用残高取得
