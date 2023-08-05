from cryptocmp import decorators


@decorators.response_error_raise
@decorators.get('data/price')
def get(
        coin,
        in_coins,
        try_conversion=None,
        exchange=None,
        extra_params=None,
        sign=None,
):
    """Get the current price of any coin in any other coin(s).

    If the crypto does not trade directly, BTC will be used for conversion.
    If the opposite pair trades, CryptoCompare inverts it (eg.: BTC-XMR)

    :param coin:
        Coin to get price of, e.g. 'BTC'.
        [Max character length: 10]

    :param in_coins:
        List of coins/currencies get price in.
        Can be a string representing comma separated list of coin/currency
        symbols (e.g. 'BTC,ETH,USD') or python list/tuple
        (e.g. ('BTC', 'ETH', 'USD').

    :param try_conversion:
        If set to false, it will try to get only direct trading values.

    :param exchange:
        The exchange to obtain data from
        (CryptoCompare aggregated average - CCCAGG - by default).
        [Max character length: 30]

    :param extra_params:
        The name of your application.
        (recommended to send it) [Max character length: 2000]

    :param sign:
        If set to true, the server will sign the requests
        (by default CryptoCompare doesn't sign them),
        this is useful for usage in smart contracts.

    :return:
        Dictionary of prices with appropriate coin symbols as keys.

        Example:

        cryptocmp.price.single.get('BTC', ('USD','JPY','EUR'))

        {
            'USD': 6114.94,

            'JPY': 679420.45,

            'EUR': 5373.64,
        }

    """

    if isinstance(in_coins, (tuple, list)):
        in_coins = ','.join(in_coins)

    return {
        'tryConversion': try_conversion,
        'fsym': coin,
        'tsyms': in_coins,
        'e': exchange,
        'extraParams': extra_params,
        'sign': sign,
    }
