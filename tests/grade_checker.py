import unittest
from activities.grade_checker import get_grade

class TestGetGrade(unittest.TestCase):
    def test_get_grade(self):
        self.assertEqual(get_grade(95), "A")
        self.assertEqual(get_grade(85), "B")
        self.assertEqual(get_grade(72), "C")
        self.assertEqual(get_grade(61), "D")
        self.assertEqual(get_grade(50), "F")
