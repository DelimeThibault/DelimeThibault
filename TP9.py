from TP7 import Fraction
import unittest


class FractionTestCase(unittest.TestCase):
    def test_numerator_positive(self):
        self.assertEqual(str(Fraction(1, 2)), "1/2")
        self.assertEqual(str(Fraction(1, -5)), "-1/5")
        self.assertEqual(str(Fraction(1, -1)), "-1")
        self.assertEqual(str(Fraction(1, 3)), "1/3")

    def test_numerator_negative(self):
        self.assertEqual(str(Fraction(-1, 2)), "-1/2")
        self.assertEqual(str(Fraction(-5, 3)), "-5/3")
        self.assertEqual(str(Fraction(-1, 1)), "-1")
        self.assertEqual(str(Fraction(-1, 3)), "-1/3")

    def test_numerator_null(self):
        self.assertEqual(str(Fraction(0, 2)), "0")
        self.assertEqual(str(Fraction(0, -5)), "0")
        self.assertEqual(str(Fraction(0, -1)), "0")
        self.assertEqual(str(Fraction(0, 3)), "0")

    def test_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 0)

        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)

        with self.assertRaises(ZeroDivisionError):
            Fraction(5, 0)

        with self.assertRaises(ZeroDivisionError):
            Fraction(-8, 0)

        with self.assertRaises(ZeroDivisionError):
            Fraction(-1, 0)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            Fraction(0.1, 2.8)
        with self.assertRaises(ValueError):
            Fraction("Thibault", "Delime")
        with self.assertRaises(ValueError):
            Fraction(None, None)
        with self.assertRaises(ValueError):
            Fraction(1, 1.5)

    def test_mixed_number(self):
        self.assertEqual(Fraction(1, 2).as_mixed_number(), "1/2")
        self.assertEqual(Fraction(1, 1).as_mixed_number(), "1")
        self.assertEqual(Fraction(8, 2).as_mixed_number(), "4")
        self.assertEqual(Fraction(4, 3).as_mixed_number(), "1 + 1/3")

    def test_addition(self):
        self.assertEqual(Fraction(1, 2) + Fraction(1, 2), Fraction(1, 1))
        self.assertEqual(Fraction(0, 2) + Fraction(1, 2), Fraction(1, 2))
        self.assertEqual(Fraction(-5, 2) + Fraction(5, -2), Fraction(-5, 1))
        self.assertEqual(Fraction(2, 3) + Fraction(5, 2), Fraction(19, 6))

    def test_subtraction(self):
        self.assertEqual(Fraction(1, 2) - Fraction(1, 2), Fraction(0, 2))
        self.assertEqual(Fraction(1, -2) - Fraction(0, 2), Fraction(-1, 2))
        self.assertEqual(Fraction(2, 3) - Fraction(1, 2), Fraction(1, 6))
        self.assertEqual(Fraction(2, 4) - Fraction(1, 4), Fraction(1, 4))

    def test_multiplication(self):
        self.assertEqual(Fraction(1, 2) * Fraction(1, 2), Fraction(1, 4))
        self.assertEqual(Fraction(1, 2) * Fraction(1, 4), Fraction(1, 8))
        self.assertEqual(Fraction(1, -2) * Fraction(1, 6), Fraction(-1, 12))
        self.assertEqual(Fraction(2, 6) * Fraction(0, 4), Fraction(0, 1))

    def test_truedivision(self):
        self.assertEqual(Fraction(1, 2) / Fraction(1, 2), Fraction(1, 1))
        self.assertEqual(Fraction(1, 2) / Fraction(1, 4), Fraction(2, 1))
        self.assertEqual(Fraction(1, -2) / Fraction(1, 6), Fraction(-3, 1))
        self.assertEqual(Fraction(2, 6) / Fraction(3, 4), Fraction(4, 9))

    def test_division_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 2) / Fraction(0, 3)
        with self.assertRaises(ZeroDivisionError):
            Fraction(5, 8) / Fraction(0, 8)
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 4) / Fraction(0, 4)

    def test_power(self):
        self.assertEqual(pow(Fraction(1, 2), 0), Fraction(1, 1))
        self.assertEqual(pow(Fraction(1, -2), -1), Fraction(-2, 1))
        self.assertEqual(pow(Fraction(1, 2), -1), Fraction(2, 1))
        self.assertEqual(pow(Fraction(5, 3), -1), Fraction(3, 5))

    def test_power_zero(self):
        with self.assertRaises(ZeroDivisionError):
            pow(Fraction(0, 3), -2)

        with self.assertRaises(ZeroDivisionError):
            pow(Fraction(0, 2), -1)

    def test_is_equal(self):
        self.assertEqual(Fraction(1, 2) == Fraction(8, 16), True)
        self.assertEqual(Fraction(2, 4) == Fraction(1, 2), True)
        self.assertEqual(Fraction(1, 2) == Fraction(1, 4), False)
        self.assertEqual(Fraction(1, 3) == Fraction(2, 3), False)

    def test_float(self):
        self.assertEqual(float(Fraction(1, 2)), 0.5)
        self.assertEqual(float(Fraction(2, 3)), 0.6666666666666666)
        self.assertEqual(float(Fraction(0, 2)), 0)
        self.assertEqual(float(Fraction(1, -2)), -0.5)

    def test_is_zero(self):
        self.assertEqual(Fraction(1, 2).is_zero(), False)
        self.assertEqual(Fraction(2, 3).is_zero(), False)
        self.assertEqual(Fraction(0, 2).is_zero(), True)
        self.assertEqual(Fraction(0, 3).is_zero(), True)

    def test_is_integer(self):
        self.assertEqual(Fraction(1, 2).is_integer(), False)
        self.assertEqual(Fraction(6, 9).is_integer(), False)
        self.assertEqual(Fraction(12, 3).is_integer(), True)
        self.assertEqual(Fraction(4, 1).is_integer(), True)

    def test_is_proper(self):
        self.assertEqual(Fraction(1, 2).is_proper(), True)
        self.assertEqual(Fraction(1, 3).is_proper(), True)
        self.assertEqual(Fraction(8, 4).is_proper(), False)
        self.assertEqual(Fraction(6, 2).is_proper(), False)

    def test_is_unit(self):
        self.assertEqual(Fraction(1, 2).is_unit(), True)
        self.assertEqual(Fraction(2, 3).is_unit(), False)
        self.assertEqual(Fraction(1, 8).is_unit(), True)
        self.assertEqual(Fraction(5, 2).is_unit(), False)

    def test_is_adjacent_to(self):
        self.assertEqual(Fraction(1, 3).is_adjacent_to(Fraction(1, 4)), True)
        self.assertEqual(Fraction(3, 4).is_adjacent_to(Fraction(2, 3)), True)
        self.assertEqual(Fraction(1, 3).is_adjacent_to(Fraction(2, 3)), False)
        self.assertEqual(Fraction(1, 3).is_adjacent_to(Fraction(1, 5)), False)


if __name__ == "__main__":
    unittest.main()
