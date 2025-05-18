import sys
import unittest
from io import StringIO

from hello import print_hello


class TestHelloWorld(unittest.TestCase):
    def test_print_hello(self):
        """Test that print_hello() outputs 'Hello, World!'."""
        # Redirect stdout to capture the printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        print_hello()

        # Reset stdout back to original
        sys.stdout = sys.__stdout__

        # Check if the output matches expected
        self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
