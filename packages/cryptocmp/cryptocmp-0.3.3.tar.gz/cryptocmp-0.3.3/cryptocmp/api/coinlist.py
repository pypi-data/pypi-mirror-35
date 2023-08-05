from cryptocmp import decorators


@decorators.extract_data
@decorators.response_error_raise
@decorators.get('data/all/coinlist')
def get(
        built_on=None,
        extra_params=None,
        sign=None,
):
    """
    Returns all the coins that CryptoCompare has added to the website.

    This is not the full list of coins in the system, it is just the list of
    coins CryptoCompare has done some research on.

    :param built_on:
        The platform that the token is built on. [Max character length: 10]
    :param extra_params:
        The name of your application (recommended to send it).
        [Max character length: 2000]
    :param sign:
        If set to true, the server will sign the requests
        (by default CryptoCompare doesn't sign them),
        this is useful for usage in smart contracts.
    :return:
        List of available coins in CryptoCompare.
    """

    return {
        'builtOn': built_on,
        'extraParams': extra_params,
        'sign': sign,
    }
