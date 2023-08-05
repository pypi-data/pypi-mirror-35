import cryptocmp.api.historical.price.minutes
import unittest


class MinutesTestCase(unittest.TestCase):
    def test_common(self):
        limit = 2
        data = cryptocmp.api.historical.price.minutes.get('BTC', 'ETH', limit=limit)
        self.assertEqual(limit, len(data))
