import unittest

from pricing import apply_discount, subtotal


class SubtotalTests(unittest.TestCase):
    def test_sums_quantity_times_price(self):
        self.assertEqual(subtotal([(2, 5.0), (1, 3.5)]), 13.5)

    def test_empty_order_is_zero(self):
        self.assertEqual(subtotal([]), 0)


class ApplyDiscountTests(unittest.TestCase):
    def test_takes_percent_off(self):
        self.assertEqual(apply_discount(200.0, 25), 150.0)

    def test_rejects_percent_out_of_range(self):
        with self.assertRaises(ValueError):
            apply_discount(100.0, 120)


if __name__ == "__main__":
    unittest.main()
