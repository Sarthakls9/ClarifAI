import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Load Hugging Face NLP model pipeline for misinformation/fact-checking
fact_checker = pipeline("text-classification", model="typeform/distilbert-base-uncased-mnli")

def scrape_webpage_content(url: str) -> str:
    """
    Scrapes text content from a webpage and returns the concatenated text.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        # Extract visible text from webpage (remove scripts, styles, etc.)
        for element in soup(["script", "style", "nav", "footer", "header"]):
            element.decompose()

        text = " ".join(soup.stripped_strings)
        return text[:5000]  # Limit to 5000 characters for analysis

    except Exception as e:
        return f"Error scraping content: {str(e)}"


def analyze_link_content(url: str):
    """
    Analyze the text content from a given URL for misinformation and return trust scores.
    """
    try:
        content = scrape_webpage_content(url)

        if content.startswith("Error"):
            return {"trust_score": 0, "details": content}

        # Run fact-check analysis on the text
        results = fact_checker(content)

        # Trust scoring logic based on the model's output
        label = results[0]["label"]
        confidence = results[0]["score"]

        if label == "ENTAILMENT":
            trust_score = int(confidence * 100)
            message = f"Webpage content appears credible ({trust_score}% confidence)."
        else:
            trust_score = int((1 - confidence) * 100)
            message = f"Potential misinformation detected. Trust score: {trust_score}%."

        return {
            "trust_score": trust_score,
            "details": message
        }

    except Exception as e:
        return {"trust_score": 0, "details": f"Link analysis failed: {str(e)}"}
