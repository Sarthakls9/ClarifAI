# tests/backend/test_link_analysis.py
import unittest
import requests

class TestLinkAnalysis(unittest.TestCase):

    def test_link_analysis_success(self):
        data = {"link": "https://example.com/suspicious-link"}
        response = requests.post("http://localhost:5000/api/analyze-link", json=data)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIn('trust_score', result)  # Assuming trust_score is part of the response

    def test_link_analysis_failure(self):
        data = {"link": "https://example.com/valid-link"}
        response = requests.post("http://localhost:5000/api/analyze-link", json=data)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIn('trust_score', result)

if __name__ == '__main__':
    unittest.main()
