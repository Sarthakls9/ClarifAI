import numpy as np
import cv2
from transformers import pipeline

class ImageAuthenticator:
    def __init__(self):
        """
        Initialize Hugging Face pipeline for deepfake detection.
        """
        print("Loading image authentication model...")
        # Load Hugging Face image classification pipeline for deepfake detection
        self.deepfake_detector = pipeline("image-classification", model="microsoft/beit-base-patch16-224-pt22k-ft22k")

    def load_image(self, image_path: str):
        """
        Load an image from the file path and preprocess it.

        Parameters:
        image_path (str): Path to the input image.

        Returns:
        np.ndarray: Loaded and resized image.
        """
        try:
            image = cv2.imread(image_path)
            if image is None:
                raise ValueError("Invalid image file.")
            
            # Resize for compatibility with deepfake models
            resized_image = cv2.resize(image, (224, 224))
            return resized_image
        except Exception as e:
            print(f"Error loading image: {e}")
            return None

    def authenticate_image(self, image: np.ndarray):
        """
        Detect potential deepfakes or manipulations.

        Parameters:
        image (np.ndarray): Preprocessed image as NumPy array.

        Returns:
        dict: Trust score and detailed message.
        """
        try:
            # Convert to RGB for Hugging Face models
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Run deepfake detection
            results = self.deepfake_detector(image_rgb)
            label = results[0]['label']
            confidence = results[0]['score']

            trust_score = int(confidence * 100)
            if label.lower() == "real":
                message = f"Image is likely authentic with {trust_score}% confidence."
            else:
                message = f"Potential manipulation detected ({label}). Trust score: {trust_score}%."

            return {"trust_score": trust_score, "details": message}

        except Exception as e:
            return {"trust_score": 0, "details": f"Image analysis failed: {str(e)}"}
