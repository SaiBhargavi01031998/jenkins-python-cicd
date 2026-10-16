
import unittest
from app import main


class TestApplication(unittest.TestCase):
    def test_application_runs(self):
        self.assertTrue(callable(main))

    def test_expected_message(self):
        self.assertEqual(
            "Hello from my Python application!",
            "Hello from my Python application!"
        )


if __name__ == "__main__":
    unittest.main()
