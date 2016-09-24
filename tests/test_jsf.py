import unittest
from datetime import datetime
from pyjsf import JSF

sd = datetime(2016, 9, 21)
ed = datetime(2016, 9, 21)


class TestJsf(unittest.TestCase):
    def setUp(self):
        self.myJSF = JSF(sd, ed)

    def test_pcsl(self):
        df = self.myJSF.pcsl()
        expected = float(272)
        actual = df.loc[(sd, '1301')]['貸借値段（円）']
        actual = float(actual)
        self.assertEqual(expected, actual)

    def test_balance(self):
        df = self.myJSF.balance()
        expected = float(4000)
        actual = df.loc[(sd, '1301')]['融資新規']
        actual = float(actual)
        self.assertEqual(expected, actual)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestJsf))
    return suite


if __name__ == '__main__':
    unittest.main()
