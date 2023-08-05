from warnings import warn

import cryptocmp.api.price.single
import cryptocmp.coin
import datetime

MINUTE = datetime.timedelta(minutes=1)
HOUR = datetime.timedelta(hours=1)
DAY = datetime.timedelta(days=1)

_time_units = {
    'minute': MINUTE,
    'hour': HOUR,
    'day': DAY,
}


def _price_history_getter(time_unit):
    getter = None
    if time_unit is DAY:
        import cryptocmp.api.historical.price.days
        getter = cryptocmp.api.historical.price.days.get
    elif time_unit is HOUR:
        import cryptocmp.api.historical.price.hours
        getter = cryptocmp.api.historical.price.hours.get
    elif time_unit is MINUTE:
        import cryptocmp.api.historical.price.minutes
        getter = cryptocmp.api.historical.price.minutes.get
    return getter


def _coin(coin_or_symbol):
    if isinstance(coin_or_symbol, str):
        coin = cryptocmp.coin.Coin(coin_or_symbol)
    elif isinstance(coin_or_symbol, cryptocmp.coin.Coin):
        coin = coin_or_symbol
    else:
        raise TypeError
    return coin


class CoinPair:
    """
    Provides access to CryptoCompare API in OOP style. Intended to be more
    user friendly and straightforward.
    """

    def __init__(self, first, second):
        self.first = _coin(first)
        self.second = _coin(second)

    def price(self, try_conversion=None, exchange=None, extra_params=None,
              sign=None):
        """Get the current price of the first currency in the second currency.

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

        :return: Current price for this pair.
        """

        price_dict = cryptocmp.api.price.single.get(
            self.first.symbol,
            self.second.symbol,
            try_conversion=try_conversion,
            exchange=exchange,
            extra_params=extra_params,
            sign=sign,
        )
        return price_dict[self.second.symbol]

    def price_history(self, time_from=None, time_to=None, time_unit=None,
                      points_num=None, exchange=None, extra_params=None,
                      sign=None, try_conversion=None):
        """Get CryptoCompare daily, hourly or minutely historical OHLCV data.

        **Description**

        Determines which API call is suitable for the passed arguments and
        adapts them to API arguments keeping request semantic.

        **API call determination**

        When passed arguments are sufficient to imply the time scale
        (aka time_unit) it is implied and used to decide which API call to use.

        **Arguments adaptation**

        When passed arguments are sufficient to imply the time range, it is
        implied and adopted using API call arguments: to_timestamp and limit.

        **Defaults**

        - Semantically (not always syntactically), time_to defaults to now.

        - time_unit defaults to day if it can not be implied.


        :param datetime.datetime time_from:
            Lower bound of time range to get historical data from.

        :param datetime.datetime time_to:
            Upper bound of time range to get historical data from.

        :param Union[datetime.timedelta, str] time_unit:
            The amount of time between data points.

            Can be any instance of timedelta. Minimum 1 minute.

            Can also be str (one of 'day', 'hour', 'minute').

        :param exchange:
            The exchange to obtain data from
            (CryptoCompare aggregated average - CCCAGG - by default).
            [Max character length: 30]

        :param points_num:
            The number of data points to return. It is always more than 1.

        :param extra_params:
            The name of your application (recommended to send it).
            [Max character length: 2000]

        :param sign:
            If set to true, the server will sign the requests
            (by default CryptoCompare doesn't sign them),
            this is useful for usage in smart contracts.

        :param try_conversion:
            If set to false, it will try to get only direct trading values.

        :return:
            CryptoCompare historical OHLCV data.

        :rtype: dict

        :Example:
        ::

            >>> CoinPair('BTC', 'USD').price_history(points_num=2)
            [
                {
                    'time': 1534291200,
                    'close': 6274.22,
                    'high': 6620.07,
                    'low': 6193.63,
                    'open': 6199.63,
                    'volumefrom': 132926.33,
                    'volumeto': 852103141.83
                },
                {
                    'time': 1534377600,
                    'close': 6439.39,
                    'high': 6439.39,
                    'low': 6217.33,
                    'open': 6274.22,
                    'volumefrom': 24013.18,
                    'volumeto': 152446768.26
                }
            ]
        """

        aggregate = None

        if time_from is not None:

            if time_to is None:
                time_to = datetime.datetime.now()

            time_period = time_to - time_from

            if points_num is not None:
                # we can imply time_unit ourselves
                if time_unit is not None:
                    raise RuntimeError('time_unit, time_from and points_num '
                                       'must not be specified together')
                time_unit = time_period / points_num

                # limit the output according to points_num
                limit = points_num
            else:
                # limit the output according to time_period
                limit = time_period // time_unit
        else:
            limit = points_num

        if isinstance(time_unit, datetime.timedelta):
            if time_unit < MINUTE:
                warn('Time unit less than 1 minute is currently not supported.'
                     'Using the minimum time unit of 1 minute instead.')
                time_unit = MINUTE
            elif time_unit < HOUR:
                aggregate = time_unit.total_seconds() / 60
                time_unit = MINUTE
            elif time_unit < DAY:
                aggregate = time_unit.total_seconds() / 3600
                time_unit = HOUR
            else:
                aggregate = time_unit.days
                time_unit = DAY
        elif isinstance(time_unit, str):
            try:
                time_unit = _time_units[time_unit]
            except KeyError:
                raise ValueError('Unknown time_unit: %s' % time_unit)
        elif time_unit is None:
            # default to day
            time_unit = DAY
        else:
            raise TypeError('Unsupported type of time_unit: %s' %
                            type(time_unit))

        price_history_getter = _price_history_getter(time_unit)

        to_timestamp = None if time_to is None else int(time_to.timestamp())

        return price_history_getter(
            coin=self.first.symbol,
            in_coin=self.second.symbol,
            to_timestamp=to_timestamp,
            limit=limit,
            exchange=exchange,
            aggregate=aggregate,
            extra_params=extra_params,
            sign=sign,
            try_conversion=try_conversion,
        )

    def __str__(self):
        return '%s/%s' % (self.first, self.second)

    def __getitem__(self, item):
        if isinstance(item, int):
            if item == 0:
                return self.first
            elif item == 1:
                return self.second
            else:
                raise IndexError
        raise TypeError

    def __reversed__(self):
        return CoinPair(self.second, self.first)
