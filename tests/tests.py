import unittest
from pandas import DataFrame,to_numeric
from binance_bot_helper import klines_to_ohlvc
from binance.client import Client

class DemoTestCase(unittest.TestCase):

    def setUp(self):
        self.klines = Client().get_historical_klines(symbol='BTCUSDT',interval='1M',start_str='2017-08-01', end_str='2021-12-01', limit=1000)

    def test_klines_to_ohlvc_columns(self):
        ''' validate number of columns '''
        ohlcv = klines_to_ohlvc(self.klines)
        self.assertEqual(len(ohlcv.columns), 7)

    def test_klines_to_ohlvc_rows(self):
        ''' validate number of rows '''
        ohlcv = klines_to_ohlvc(self.klines)
        self.assertEqual(len(ohlcv), 53)

if __name__ == '__main__':
    unittest.main()