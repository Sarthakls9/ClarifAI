from transformers import pipeline

class NLPModel:
    def __init__(self):
        """
        Initialize NLP pipelines from Hugging Face.
        """
        print("Loading NLP models...")
        # Load Hugging Face model pipelines
        self.fact_checker = pipeline("text-classification", model="typeform/distilbert-base-uncased-mnli")
        self.text_analyzer = pipeline("text-generation", model="gpt2")

    def analyze_text(self, text: str):
        """
        Perform text analysis to detect misinformation or inconsistencies.

        Parameters:
        text (str): The input text for analysis.

        Returns:
        dict: Analysis result with label and confidence score.
        """
        print("Running fact-check analysis...")
        try:
            results = self.fact_checker(text)
            label = results[0]["label"]
            confidence = results[0]["score"]

            if label == "ENTAILMENT":
                trust_score = int(confidence * 100)
                message = f"Text appears credible ({trust_score}% confidence)."
            else:
                trust_score = int((1 - confidence) * 100)
                message = f"Potential misinformation detected. Trust score: {trust_score}%."

            return {"trust_score": trust_score, "details": message}
        
        except Exception as e:
            return {"trust_score": 0, "details": f"Text analysis failed: {str(e)}"}

    def generate_summary(self, text: str, max_length: int = 50):
        """
        Generate a textual summary using text generation models.

        Parameters:
        text (str): The input text to summarize.
        max_length (int): Maximum length of the summary.

        Returns:
        str: Generated summary text.
        """
        print("Generating summary...")
        try:
            generated_text = self.text_analyzer(text, max_length=max_length, num_return_sequences=1)
            return generated_text[0]["generated_text"]
        
        except Exception as e:
            return f"Summary generation failed: {str(e)}"
