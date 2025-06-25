import unittest
from activities.fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(1), ["1"])
        self.assertEqual(fizzbuzz(3), ["1", "2", "Fizz"])
        self.assertEqual(fizzbuzz(5), ["1", "2", "Fizz", "4", "Buzz"])
        self.assertEqual(fizzbuzz(15), [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz"
        ])
