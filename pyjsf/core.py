# -*- coding: utf-8 -*-
import pandas as pd
from pyjsf.data.download import download_csv
from pyjsf.data.jsfurl import CreateUrlShina, CreateUrlZandaka


class JSF:
    """
    Pythonで日本証券金融の品貸料、信用残高を取得するクラス
    """
    def __init__(self, date_from, date_to):
        self.date_from = date_from
        self.date_to = date_to

    def pcsl(self):

        urls = CreateUrlShina(self.date_from, self.date_to).urls()
        df = self._download(urls)

        if df.empty:
            return df

        df['貸借申込日'] = pd.to_datetime(df['貸借申込日'], format='%Y%m%d')
        df['決済日'] = pd.to_datetime(df['決済日'], format='%Y%m%d')
        df = df.set_index(keys=['貸借申込日', 'コード'], drop=True)
        return df

    def balance(self):
        urls = CreateUrlZandaka(self.date_from, self.date_to).urls()
        df = self._download(urls)

        if df.empty:
            return df

        df['申込日'] = pd.to_datetime(df['申込日'], format='%Y/%m/%d')
        df = df.set_index(keys=['申込日', 'コード'], drop=True)
        return df

    @staticmethod
    def _download(urls):
        # 取得対象URLを順次取得して結合
        dfs = []
        for url in urls:
            df = download_csv(url)
            dfs.append(df)
        else:
            df = pd.concat(dfs)
        return df
