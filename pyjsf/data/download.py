# -*- coding: utf-8 -*-
import time
import urllib.error
import urllib.request

import pandas as pd
import numpy as np

_SLEEP_TIME = 2


def download_csv(url) -> pd.DataFrame:
    """
    urlで指定したデータをDataFrameで取得する. 取得可能でなければ空のDataFrameを返す
    :param url:
    :return:
    """
    try:
        dtypes = {'コード': np.object}
        df = pd.read_csv(urllib.request.urlopen(url), encoding='Shift-JIS', skiprows=4, dtype=dtypes)
    except pd.parser.CParserError:
        df = pd.DataFrame()
    finally:
        time.sleep(_SLEEP_TIME)
    return df
