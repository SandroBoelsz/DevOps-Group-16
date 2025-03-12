# Install pytest before running:            pip install requests pytest
# Run tests by running:                     pytest test_api.py -v
# Alternative command for running tests:    python -m unittest test_api.py

import unittest
import requests

class TestPytest(unittest.TestCase):
    def test_pytest_works(self):
        self.assertEqual(1, 1)

class TestAPI(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5001"

    def test_trigger_method_not_allowed(self):
        url = f"{self.BASE_URL}/workflow-data-replication/trigger"
        response = requests.get(url)  
        expected_status = 405  # We expect method not allowed
        expected_message = {"message": "The method is not allowed for the requested URL."}

        self.assertEqual(response.status_code, expected_status)
        self.assertEqual(response.json(), expected_message)

if __name__ == "__main__":
    unittest.main()
