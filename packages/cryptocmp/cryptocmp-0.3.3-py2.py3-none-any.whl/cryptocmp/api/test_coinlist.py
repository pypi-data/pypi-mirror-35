import unittest
import cryptocmp.api.coinlist


class CoinListTestCase(unittest.TestCase):

    def test_common(self):
        coins = cryptocmp.api.coinlist.get()
        # popular coins should be in the list
        self.assertIn('BTC', coins)
        self.assertIn('ETH', coins)
        self.assertIn('LTC', coins)
