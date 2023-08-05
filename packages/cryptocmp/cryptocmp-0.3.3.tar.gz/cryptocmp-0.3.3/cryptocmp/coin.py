import cryptocmp.api.coinlist
import cryptocmp.api.price.single
import cryptocmp.coin_pair
from cryptocmp.exceptions import CoinDoesntExist


class Coin:
    """
    Provides access to CryptoCompare API in OOP style. Intended to be more
    user friendly and straightforward.
    """

    @staticmethod
    def all():
        """
        :returns: A set of all coin symbols available in CryptoCompare coin
            list API call.
        """

        return set(cryptocmp.api.coinlist.get().keys())

    def __init__(self, symbol, check_exists=False):
        """
        Instantiates a coin object with specified symbol. By default no symbol
        check is run to avoid extra traffic and slowdown.

        :param symbol: str identifying the coin (e.g. 'BTC', 'ETH').

        :param check_exists:
            when set to True triggers a lookup of the symbol in Coin.all() set

        :raises: CoinDoesntExist if lookup of the specified symbol fails.
        """

        self.symbol = symbol
        if check_exists:
            self.check_exists()

    def check_exists(self):
        """
        Performs a lookup of the symbol in Coin.all() set.

        :raises: CoinDoesntExist if this coin symbol does not exist.
        """

        exists = self.symbol in self.all()
        if not exists:
            raise CoinDoesntExist

    def price(self, in_coins=None):
        """
        Get the current price(s) of this coin in specified coin(s).

        :param in_coins:
            The coin(s)/currency(ies) to get the price in.

            Each 'coin' here is either a str representing its symbol
            (e.g. 'BTC') or coin object.

            Can be a single coin or list/tuple of coins.

        :return:
            If in_coins is instance list or tuple then the dict of prices of
            this coin in conversion to specified coins.
            Keys are the specified coin symbols. Values are the prices.

            Otherwise, the singe current conversion price of this coin into the
            specified currency.
        """

        return_single_coin_price = False
        if isinstance(in_coins, str):
            return_single_coin_price = ',' not in in_coins
        elif isinstance(in_coins, Coin):
            in_coins = in_coins.symbol
            return_single_coin_price = True
        elif isinstance(in_coins, (list, tuple)):
            if all(isinstance(coin, Coin) for coin in in_coins):
                in_coins = (coin.symbol for coin in in_coins)
        else:
            raise TypeError("Unsupported type of the argument 'in_coins'")

        ret = cryptocmp.api.price.single.get(self.symbol, in_coins)

        if return_single_coin_price:
            ret = ret[in_coins]

        return ret

    def to(self, coin):
        return cryptocmp.coin_pair.CoinPair(self, coin)

    def __str__(self):
        return self.symbol
