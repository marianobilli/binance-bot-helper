import pytest
from pandas import DataFrame,to_numeric
from binance_bot_helper import klines_to_ohlvc
from binance.client import Client

@pytest.fixture()
def klines():
    print("Setup...")
    yield  Client().get_historical_klines(symbol='BTCUSDT',interval='1M',start_str='2017-08-01', end_str='2021-12-01', limit=1000)
    print("Teardown...")

class TestCases():
    def test_klines_to_ohlvc_columns(self, klines):
        ''' validate number of columns '''
        ohlcv = klines_to_ohlvc(klines)
        assert len(ohlcv.columns) == 7

    def test_klines_to_ohlvc_rows(self, klines):
        ''' validate number of rows '''
        ohlcv = klines_to_ohlvc(klines)
        assert len(ohlcv) == 53