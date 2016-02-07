#! /usr/bin/env python
# -*- coding: utf-8 -*-
# python 3.5
import urllib.request
import pandas as pd
import datetime


class PyJSF:
    """
    Pythonで日本証券金融の品貸料、信用残高を取得するクラス
    """
    def __init__(self, date=datetime.datetime.today()):
        k = ['y', 'm', 'd']
        v = [str(date.year), str(date.month).zfill(2), str(date.day).zfill(2)]
        self.args = dict(zip(k, v))

    def shina(self):
        # URL生成
        url = 'http://www.jsf.co.jp/de/stock/dlcsv.php?target=pcsl&date={y}-{m}-{d}'.format(**self.args)
        response = urllib.request.urlopen(url)

        # データを取得しDataFrameに追加
        try:
            df = pd.read_csv(response, encoding='Shift_JIS', skiprows=3)
        except pd.parser.CParserError:
            df = pd.DataFrame()

        return df

    def balance(self):
        # URL生成
        url = 'http://www.jsf.co.jp/de/stock/dlcsv.php?target=balance&date={y}-{m}-{d}'.format(**self.args)
        response = urllib.request.urlopen(url)

        # データを取得しDataFrameに追加
        try:
            df = pd.read_csv(response, encoding='Shift_JIS', skiprows=3)
        except pd.parser.CParserError:
            df = pd.DataFrame()

        return df

if __name__ == '__main__':
    d = datetime.datetime(2016, 1, 4)
    myJSF = PyJSF(d)
    print(myJSF.shina())    # 品貸料率取得
    print(myJSF.balance())  # 信用残高取得
