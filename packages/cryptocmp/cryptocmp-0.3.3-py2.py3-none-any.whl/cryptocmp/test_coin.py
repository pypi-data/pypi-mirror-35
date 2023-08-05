import unittest

from cryptocmp.coin import Coin
from cryptocmp.exceptions import CoinDoesntExist


class CoinTestCase(unittest.TestCase):

    def test_list(self):
        coins = Coin.all()
        # popular coins should be in the list
        self.assertIn('BTC', coins)
        self.assertIn('ETH', coins)
        self.assertIn('LTC', coins)

    def test_init_absent_coin(self):
        # Hopefully there is never gonna be a valid coin with empty name
        absent_coin_symbol = ''
        with self.assertRaises(CoinDoesntExist):
            Coin(absent_coin_symbol, check_exists=True)

    @staticmethod
    def test_init():
        # Assumption: BTC lives forever
        Coin('BTC', check_exists=True)
        # Assumption: ETH lives forever
        Coin('ETH', check_exists=True)

    def test_price_single_coin(self):
        # cannot know exactly the price so check for common sense
        bitcoin = Coin('BTC')
        self.assertEqual(1, bitcoin.price(bitcoin),
                         "1 BTC != 1 BTC or passing coin object doesn't work")
        ether = Coin('ETH')
        self.assertEqual(1, ether.price('ETH'),
                         "1 ETH != 1 ETH or passing coin symbol doesn't work")
        self.assertLessEqual(0, ether.price(bitcoin),
                             "Price cannot be negative")
