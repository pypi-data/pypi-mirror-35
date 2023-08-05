from unittest import TestCase
import cryptocmp.api.price.single


class SinglePriceTestCase(TestCase):
    def test_single(self):
        data = cryptocmp.api.price.single.get('BTC', 'USD')
        self.assertIsInstance(data, dict)
        self.assertIn('USD', data)
        del data['USD']
        self.assertDictEqual(dict(), data,
                             'result contains more than requested')

    def test_single_tuple(self):
        data = cryptocmp.api.price.single.get('BTC', ('USD',))
        self.assertIsInstance(data, dict)
        self.assertIn('USD', data)
        del data['USD']
        self.assertDictEqual(dict(), data,
                             'result contains more than requested')

    def test_single_list(self):
        data = cryptocmp.api.price.single.get('BTC', ['USD'])
        self.assertIsInstance(data, dict)
        self.assertIn('USD', data)
        del data['USD']
        self.assertDictEqual(dict(), data,
                             'result contains more than requested')

    def test_multiple_comma_separated_string(self):
        data = cryptocmp.api.price.single.get('BTC', 'USD,EUR')
        self.assertIsInstance(data, dict)
        self.assertIn('USD', data)
        self.assertIn('EUR', data)
        del data['USD']
        del data['EUR']
        self.assertDictEqual(dict(), data,
                             'result contains more than requested')

    def test_multiple_tuple(self):
        data = cryptocmp.api.price.single.get('BTC', ('USD', 'EUR'))
        self.assertIsInstance(data, dict)
        self.assertIn('USD', data)
        self.assertIn('EUR', data)
        del data['USD']
        del data['EUR']
        self.assertDictEqual(dict(), data,
                             'result contains more than requested')

    def test_multiple_list(self):
        data = cryptocmp.api.price.single.get('BTC', ['USD', 'EUR'])
        self.assertIsInstance(data, dict)
        self.assertIn('USD', data)
        self.assertIn('EUR', data)
        del data['USD']
        del data['EUR']
        self.assertDictEqual(dict(), data,
                             'result contains more than requested')
