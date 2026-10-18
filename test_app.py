import unittest
from app import add, multiply, subtract


class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 20), 30)

    def test_multiply(self):
        self.assertEqual(multiply(10, 20), 200)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)


if __name__ == "__main__":
    unittest.main()