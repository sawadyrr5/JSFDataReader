import unittest
from datetime import datetime
from pyjsf import JSF

sd = datetime(2016, 8, 18)
ed = datetime(2016, 8, 18)


class TestJsf(unittest.TestCase):
    def setUp(self):
        self.myJSF = JSF(sd, ed)

    def test_pcsl(self):
        df = self.myJSF.pcsl()
        expected = float(260)
        target_date = datetime(2016, 8, 18)
        actual = df.loc[(target_date, '1301')]['貸借値段（円）']
        actual = float(actual)
        self.assertEqual(expected, actual)

    def test_balance(self):
        df = self.myJSF.balance()
        expected = float(1000)
        target_date = datetime(2016, 8, 18)
        actual = df.loc[(target_date, '1301')]['融資新規']
        actual = float(actual)
        self.assertEqual(expected, actual)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestJsf))
    return suite


if __name__ == '__main__':
    unittest.main()
