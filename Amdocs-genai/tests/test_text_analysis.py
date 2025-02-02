# tests/backend/test_text_analysis.py
import unittest
import requests

class TestTextAnalysis(unittest.TestCase):

    def test_text_analysis_success(self):
        data = {"text": "The Eiffel Tower is in Paris."}
        response = requests.post("http://localhost:5000/api/analyze-text", json=data)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIn('trust_score', result)  # Assuming trust_score is part of the response

    def test_text_analysis_failure(self):
        data = {"text": "This is a random sentence."}
        response = requests.post("http://localhost:5000/api/analyze-text", json=data)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIn('trust_score', result)

if __name__ == '__main__':
    unittest.main()
