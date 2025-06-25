import unittest
import sys
from io import StringIO
from activities.translator import translator

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
