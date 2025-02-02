from transformers import pipeline
from PIL import Image

# Load a specialized deepfake detection pipeline from Hugging Face
deepfake_detector = pipeline("image-classification", model="nateraw/deepfake-detection")

def analyze_image(image_path: str):
    """
    Analyze the image for potential deepfake or manipulation using a specialized model.
    """
    try:
        # Load the image
        image = Image.open(image_path).convert("RGB")

        # Run deepfake detection model on the image
        results = deepfake_detector(image)

        # Extract the most confident result
        top_result = max(results, key=lambda x: x["score"])
        label = top_result["label"]
        confidence_score = top_result["score"]

        # Trust scoring logic based on detection
        if label == "REAL" and confidence_score > 0.7:
            trust_score = int(confidence_score * 100)
            message = f"Image is likely authentic ({trust_score}% confidence)."
        else:
            trust_score = int((1 - confidence_score) * 100)
            message = f"Potential deepfake detected. Trust score: {trust_score}%."

        return {
            "trust_score": trust_score,
            "details": message
        }

    except Exception as e:
        return {"trust_score": 0, "details": f"Image analysis failed: {str(e)}"}
