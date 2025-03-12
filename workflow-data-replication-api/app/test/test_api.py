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
    ENDPOINT = "/workflow-data-replication/trigger"
    REQUEST_PAYLOAD = {
        "minioUrl": "https://scruffy.lab.uvalight.net:9000",
        "bucket": "naa-vre-user-data",
        "filename": "s.boelsz@gmail.com/testen.txt",
    }
    REQUEST_PAYLOAD_FILE_NOT_EXISTING = {
        "minioUrl": "https://scruffy.lab.uvalight.net:9000",
        "bucket": "naa-vre-user-data",
        "filename": "s.boelsz@gmail.com/testen1.txt",
    }

    def test_trigger_method_not_allowed(self):
        url = f"{self.BASE_URL}/workflow-data-replication/trigger"
        response = requests.get(url)  
        expected_status = 405  # We expect method not allowed
        expected_message = {"message": "The method is not allowed for the requested URL."}

        self.assertEqual(response.status_code, expected_status)
        self.assertEqual(response.json(), expected_message)

    def test_trigger_post_request_with_correct_payload(self):
        url = f"{self.BASE_URL}{self.ENDPOINT}"
        response = requests.post(url, json=self.REQUEST_PAYLOAD)
        expected_status = 200  # We expect method not allowed
        expected_message = {"message": "File already present in the Dutch S3 bucket"}  

        # Check if the response status is as expected (adjust if needed)
        self.assertEqual(response.status_code, expected_status)  
        self.assertEqual(response.json(), expected_message)

    def test_trigger_post_request_with_new_payload(self):
        url = f"{self.BASE_URL}{self.ENDPOINT}"
        response = requests.post(url, json=self.REQUEST_PAYLOAD_FILE_NOT_EXISTING)
        expected_status = 500  # Should give an error
        expected_message = {"message": "File is not present in both Spanish and Dutch S3 buckets"}  

        # Check if the response status is as expected (adjust if needed)
        self.assertEqual(response.status_code, expected_status)  
        self.assertEqual(response.json(), expected_message)

if __name__ == "__main__":
    unittest.main()
