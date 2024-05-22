import unittest

class testcalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = calculadora()

    def test_suma(self):
        self.assertEqual(self.calc.suma(3, 5), 8)
        self.assertEqual(self.calc.suma(-1, 1), 0)
        self.assertEqual(self.calc.suma(-1, -1), -2)

    def test_resta(self):
        self.assertEqual(self.calc.resta(10, 5), 5)
        self.assertEqual(self.calc.resta(-1, 1), -2)
        self.assertEqual(self.calc.resta(-1, -1), 0)

    def test_multiplicacion(self):
        self.assertEqual(self.calc.multiplicacion(3, 7), 21)
        self.assertEqual(self.calc.multiplicacion(-1, 1), -1)
        self.assertEqual(self.calc.multiplicacion(-1, -1), 1)

    def test_division(self):
        self.assertEqual(self.calc.division(10, 2), 5)
        self.assertEqual(self.calc.division(-10, 2), -5)
        self.assertEqual(self.calc.division(-10, -2), 5)
        with self.assertRaises(ValueError):
            self.calc.division(10, 0)

if __name__ == '__main__':
    unittest.main()