# Copyright (C) 2018 GuQiangJs.
# Licensed under Apache License 2.0 <see LICENSE file>

import time

import pandas as pd

__all__ = ['get_szse_symbols']

# http://www.szse.cn/szseWeb/ShowReport.szse?SHOWTYPE=xlsx&CATALOGID=1110&tab1PAGENO=1&ENCODE=1&TABKEY=tab1  全部
# http://www.szse.cn/szseWeb/ShowReport.szse?SHOWTYPE=xlsx&CATALOGID=1110&tab1PAGENO=1&ENCODE=1&TABKEY=tab2  A股
# http://www.szse.cn/szseWeb/ShowReport.szse?SHOWTYPE=xlsx&CATALOGID=1110&tab5PAGENO=1&ENCODE=1&TABKEY=tab5  中小板
# http://www.szse.cn/szseWeb/ShowReport.szse?SHOWTYPE=xlsx&CATALOGID=1110&tab6PAGENO=1&ENCODE=1&TABKEY=tab6  创业板


_ticker_cache = None


def get_szse_symbols(kind: str = '2', retry_count=3, timeout=30, pause=None):
    """获取最新的深圳证券交易所交易的 股票 名称数据

    数据来源：http://www.szse.cn/main/marketdata/jypz/colist/

    Args:
        kind: 分类。

            * 2: A股(A股中包含所有的中小板、创业板数据)
            * 5: 中小板
            * 6: 创业板

        retry_count: 重试次数
        timeout: 超时时间
        pause:

    Returns:
        ``pandas.DataFrame``:

    Examples:
        .. code-block:: python

            >>> from finance_datareader_py.szse import get_szse_symbols

            >>> print(get_szse_symbols().tail())

                  symbol   name
            2101  300743   天地数码
            2102  300745   欣锐科技
            2103  300746   汉嘉设计
            2104  300747   锐科激光
            2105  300750   宁德时代
    """
    global _ticker_cache
    if timeout < 0:
        raise ValueError(
            'timeout must be >= 0, not {timeout}'.format(timeout=timeout))

    if pause is None:
        pause = timeout / 3
    elif pause < 0:
        raise ValueError('pause must be >= 0, not {pause}'.format(pause=pause))

    if _ticker_cache is None or kind not in _ticker_cache:
        if _ticker_cache is None:
            _ticker_cache = {}
        while retry_count > 0:
            try:
                _ticker_cache[kind] = _download_szse_symbols(kind)
                retry_count = -1
            except Exception:
                # retry on any exception
                if retry_count <= 0:
                    raise
                else:
                    retry_count -= 1
                    time.sleep(pause)

    return _ticker_cache[kind]


def _download_szse_symbols(kind: str):
    url = r'http://www.szse.cn/szseWeb/ShowReport.szse?SHOWTYPE=xlsx&CATALOGID=1110&tab{0}PAGENO=1&ENCODE=1&TABKEY=tab{0}'.format(
        kind)
    df = pd.read_excel(url, convert_float=False, dtype=object)
    df = df[['公司代码', '公司简称']]
    df.rename(columns={'公司代码': 'symbol', '公司简称': 'name'}, inplace=True)
    # df.set_index("symbol", inplace=True)
    return df
