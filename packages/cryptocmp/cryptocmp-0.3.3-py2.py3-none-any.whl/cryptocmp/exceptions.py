class CryptoCompareException(Exception):
    def __init__(self, response):
        super().__init__(response['Message'])


class CoinDoesntExist(Exception):
    pass
