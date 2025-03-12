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
        response = requests.get(url)  # Assuming the route doesn't allow GET
        expected_status = 405  # Method Not Allowed
        expected_message = {"message": "The method is not allowed for the requested URL."}

        self.assertEqual(response.status_code, expected_status)
        self.assertEqual(response.json(), expected_message)

    # # def test_trigger_response_body_contains_expected_data(self):
    # #     url = f"{self.BASE_URL}/workflow-data-replication/trigger"
    # #     response = requests.post(url, json={})  # Sending an empty body or necessary payload

    # #     self.assertEqual(response.status_code, 200)  # Adjust this based on expected status
    # #     response_json = response.json()

    # #     expected_data = {
    # #         "minioUrl": "https://scruffy.lab.uvalight.net:9000",
    # #         "bucket": "naa-vre-user-data",
    # #         "filename": "s.boelsz@gmail.com/testen.txt",
    # #     }

    #     # Check if the expected data is included in the response (not necessarily a full match)
    #     for key, value in expected_data.items():
    #         self.assertIn(key, response_json)
    #         self.assertEqual(response_json[key], value)

if __name__ == "__main__":
    unittest.main()
