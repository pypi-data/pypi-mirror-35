import datetime
from unittest import TestCase

from cryptocmp.coin_pair import CoinPair, MINUTE, HOUR, DAY

MAX_TIME_ERROR = 5  # seconds


class CoinPairTestCase(TestCase):

    def test_price(self):
        pair = CoinPair('BTC', 'ETH')
        self.assertIsInstance(pair.price(), (float, int))
        self.assertGreater(pair.price(), 0)

    def test_price_history_days(self):
        pair = CoinPair('BTC', 'USD')
        points_num = 3

        now = datetime.datetime.now()
        past = now - points_num * DAY
        sub_tests = {
            "time_unit is str 'day'":
                pair.price_history(time_unit='day', points_num=points_num),

            'time_unit is timedelta DAY':
                pair.price_history(time_unit=DAY, points_num=points_num),

            'time_unit is implied from time_from, time_to and points_num':
                pair.price_history(time_from=past, time_to=now,
                                   points_num=points_num)
        }

        for sub_test_name, data in sub_tests.items():
            with self.subTest(sub_test_name):
                self.assertEqual(points_num, len(data))
                for item in data:
                    self.assertIn('open', item)
                    self.assertIn('high', item)
                    self.assertIn('low', item)
                    self.assertIn('close', item)
                    self.assertIn('volumefrom', item)
                    self.assertIn('volumeto', item)
                    self.assertIn('time', item)
                for item, next_item in zip(data[:-1], data[1:]):
                    seconds_diff = next_item['time'] - item['time']
                    self.assertLessEqual(
                        abs(seconds_diff - DAY.total_seconds()),
                        MAX_TIME_ERROR)

    def test_price_history_hours(self):
        pair = CoinPair('BTC', 'USD')
        points_num = 3

        now = datetime.datetime.now()
        past = now - points_num * HOUR
        sub_tests = {
            "time_unit is str 'hour'":
                pair.price_history(time_unit='hour', points_num=points_num),

            'time_unit is timedelta HOUR':
                pair.price_history(time_unit=HOUR, points_num=points_num),

            'time_unit is implied from time_from, time_to and points_num':
                pair.price_history(time_from=past, time_to=now,
                                   points_num=points_num)
        }

        for sub_test_name, data in sub_tests.items():
            with self.subTest(sub_test_name):
                self.assertEqual(points_num, len(data))
                for item in data:
                    self.assertIn('open', item)
                    self.assertIn('high', item)
                    self.assertIn('low', item)
                    self.assertIn('close', item)
                    self.assertIn('volumefrom', item)
                    self.assertIn('volumeto', item)
                    self.assertIn('time', item)
                for item, next_item in zip(data[:-1], data[1:]):
                    seconds_diff = next_item['time'] - item['time']
                    self.assertLessEqual(
                        abs(seconds_diff - HOUR.total_seconds()),
                        MAX_TIME_ERROR)

    def test_price_history_minutes(self):
        pair = CoinPair('BTC', 'USD')
        points_num = 3

        now = datetime.datetime.now()
        past = now - points_num * MINUTE
        sub_tests = {
            "time_unit is str 'minute'":
                pair.price_history(time_unit='minute', points_num=points_num),

            'time_unit is timedelta MINUTE':
                pair.price_history(time_unit=MINUTE, points_num=points_num),

            'time_unit is implied from time_from, time_to and points_num':
                pair.price_history(time_from=past, time_to=now,
                                   points_num=points_num)
        }

        for sub_test_name, data in sub_tests.items():
            with self.subTest(sub_test_name):
                self.assertEqual(points_num, len(data))
                for item in data:
                    self.assertIn('open', item)
                    self.assertIn('high', item)
                    self.assertIn('low', item)
                    self.assertIn('close', item)
                    self.assertIn('volumefrom', item)
                    self.assertIn('volumeto', item)
                    self.assertIn('time', item)
                for item, next_item in zip(data[:-1], data[1:]):
                    seconds_diff = next_item['time'] - item['time']
                    self.assertLessEqual(
                        abs(seconds_diff - MINUTE.total_seconds()),
                        MAX_TIME_ERROR)
