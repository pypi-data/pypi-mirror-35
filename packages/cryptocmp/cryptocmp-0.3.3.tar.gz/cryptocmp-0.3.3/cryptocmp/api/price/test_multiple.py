from unittest import TestCase
import cryptocmp.api.price.multiple


class MultiplePriceTestCase(TestCase):
    def test_single(self):
        data = cryptocmp.api.price.multiple.get('BTC', 'ETH')
        self.assertIsInstance(data, dict)
        self.assertIn('BTC', data)
        self.assertIn('ETH', data['BTC'])

    def test_single_tuple(self):
        data = cryptocmp.api.price.multiple.get(('BTC',), ('ETH',))
        self.assertIsInstance(data, dict)
        self.assertIn('BTC', data)
        self.assertIn('ETH', data['BTC'])

    def test_single_list(self):
        data = cryptocmp.api.price.multiple.get(['BTC'], ['ETH'])
        self.assertIsInstance(data, dict)
        self.assertIn('BTC', data)
        self.assertIn('ETH', data['BTC'])

    def test_multiple_tuple(self):
        data = cryptocmp.api.price.multiple.get(('BTC', 'ETH'), ('USD', 'EUR'))
        self.assertIsInstance(data, dict)
        self.assertIn('BTC', data)
        self.assertIn('ETH', data)
        self.assertIn('USD', data['BTC'])
        self.assertIn('EUR', data['BTC'])
        self.assertIn('USD', data['ETH'])
        self.assertIn('EUR', data['ETH'])

    def test_multiple_list(self):
        data = cryptocmp.api.price.multiple.get(['BTC', 'ETH'], ['USD', 'EUR'])
        self.assertIsInstance(data, dict)
        self.assertIn('BTC', data)
        self.assertIn('ETH', data)
        self.assertIn('USD', data['BTC'])
        self.assertIn('EUR', data['BTC'])
        self.assertIn('USD', data['ETH'])
        self.assertIn('EUR', data['ETH'])

    def test_multiple_comma_separated_string(self):
        data = cryptocmp.api.price.multiple.get('BTC,ETH', 'USD,EUR')
        self.assertIsInstance(data, dict)
        self.assertIn('BTC', data)
        self.assertIn('ETH', data)
        self.assertIn('USD', data['BTC'])
        self.assertIn('EUR', data['BTC'])
        self.assertIn('USD', data['ETH'])
        self.assertIn('EUR', data['ETH'])
