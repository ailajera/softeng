import unittest
from io import StringIO
import sys
from activities.list_processor import list_processor
from activities.login_system import login 
from activities.grade_checker import get_grade 
from activities.translator import translator 

class TestListProcessor(unittest.TestCase):
    def test_list_processor(self):
        numbers = [1, 2, 3]
        expected_output = "1 is odd\n2 is even\n3 is odd\n"

        captured_output = StringIO()
        sys.stdout = captured_output
        list_processor(numbers)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

class TestGetGrade(unittest.TestCase):
    def test_get_grade(self):
        self.assertEqual(get_grade(95), "A")
        self.assertEqual(get_grade(85), "B")
        self.assertEqual(get_grade(72), "C")
        self.assertEqual(get_grade(61), "D")
        self.assertEqual(get_grade(50), "F")

class TestLogin(unittest.TestCase):
    def test_login(self):
        self.assertEqual(login("admin", "1234"), "Login successful")
        self.assertEqual(login("admin", "wrong"), "Invalid credentials")
        self.assertEqual(login("user", "1234"), "Invalid credentials")

class TestTranslator(unittest.TestCase):
    def test_translator(self):
        inputs_and_expected = [
            ("hello\n", "Filipino: kamusta"),
            ("thank you\n", "Filipino: salamat"),
            ("goodbye\n", "Filipino: paalam"),
            ("unknown\n", "Filipino: Translation not found"),
        ]

        for user_input, expected in inputs_and_expected:
            sys.stdin = StringIO(user_input)
            captured_output = StringIO()
            sys.stdout = captured_output

            translator()

            sys.stdout = sys.__stdout__
            sys.stdin = sys.__stdin__

            output = captured_output.getvalue()
            self.assertIn(expected, output)

