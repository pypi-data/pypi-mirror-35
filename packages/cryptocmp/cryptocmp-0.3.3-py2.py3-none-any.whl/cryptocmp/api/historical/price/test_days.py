import unittest

import cryptocmp.api.historical.price.days


class DaysTestCase(unittest.TestCase):
    def test_common(self):
        data = cryptocmp.api.historical.price.days.get('BTC', 'USD', limit=1)
        for item in data:
            self.assertIn('open', item)
            self.assertIn('high', item)
            self.assertIn('low', item)
            self.assertIn('close', item)
            self.assertIn('volumefrom', item)
            self.assertIn('volumeto', item)
