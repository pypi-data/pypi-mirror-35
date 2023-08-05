import unittest

from followthemoney.types import phones


class PhonesTest(unittest.TestCase):

    def test_us_number(self):
        self.assertEqual(phones.clean('+1-800-784-2433'), '+18007842433')
        self.assertEqual(phones.clean('+1 800 784 2433'), '+18007842433')
        self.assertEqual(phones.clean('+18007842433'), '+18007842433')
        self.assertEqual(phones.clean('+1 555 8379'), None)

    def test_de_number(self):
        self.assertEqual(phones.clean('017623423980'), None)
        self.assertEqual(phones.clean('017623423980', countries='DE'),
                         '+4917623423980')
