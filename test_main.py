import sys
import unittest
import subprocess
import os
import sys
import io
import contextlib

class TestHello(unittest.TestCase):
    @contextlib.contextmanager
    def captured_output(self):
        new_out = io.StringIO()
        old_out = sys.stdout
        try:
            sys.stdout = new_out
            yield new_out
        finally:
            sys.stdout = old_out

    def test_hello(self):
        with self.captured_output() as captured_output:
            from main import hello
            hello()
        self.assertEqual(captured_output.getvalue().strip(), 'hi')

if __name__ == '__main__':
    unittest.main(argv=[os.path.basename(__file__)])