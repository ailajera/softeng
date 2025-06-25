import sys
import unittest
from io import StringIO
from activities.list_processor import list_processor 

class TestListProcessor(unittest.TestCase):
    def test_list_processor(self):
        numbers = [1, 2, 3]
        expected_output = "1 is odd\n2 is even\n3 is odd\n"

        captured_output = StringIO()
        sys.stdout = captured_output
        list_processor(numbers)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
