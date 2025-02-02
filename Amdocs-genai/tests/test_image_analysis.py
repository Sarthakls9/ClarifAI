# tests/backend/test_image_analysis.py
import unittest
import requests

class TestImageAnalysis(unittest.TestCase):

    def test_image_analysis_success(self):
        data = {"imageUrl": "https://example.com/suspicious_image.jpg"}
        response = requests.post("http://localhost:5000/api/analyze-image", json=data)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIn('analysis_result', result)  # Assuming the result contains analysis

    def test_image_analysis_failure(self):
        data = {"imageUrl": "https://example.com/valid_image.jpg"}
        response = requests.post("http://localhost:5000/api/analyze-image", json=data)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIn('analysis_result', result)

if __name__ == '__main__':
    unittest.main()
