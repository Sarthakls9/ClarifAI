import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from nlp_model import NLPModel

class WebPageScraper:
    def __init__(self):
        """
        Initialize the NLP model for text analysis.
        """
        self.nlp_model = NLPModel()

    def fetch_webpage_content(self, url: str) -> str:
        """
        Fetch and extract text content from a web page.

        Parameters:
        url (str): The URL of the web page.

        Returns:
        str: Extracted textual content.
        """
        print(f"Fetching content from: {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Extract textual content from relevant tags
            content = []
            for paragraph in soup.find_all("p"):
                text = paragraph.get_text(strip=True)
                if text:
                    content.append(text)
            
            return " ".join(content) if content else "No meaningful text found."
        
        except requests.RequestException as e:
            return f"Failed to fetch webpage content: {str(e)}"

    def analyze_webpage_content(self, url: str):
        """
        Analyze the content of a web page for fact-checking.

        Parameters:
        url (str): The URL of the web page.

        Returns:
        dict: Trust score and detailed analysis.
        """
        content = self.fetch_webpage_content(url)
        if "Failed" in content:
            return {"trust_score": 0, "details": content}
        
        print("Analyzing webpage content...")
        result = self.nlp_model.analyze_text(content)
        return result
