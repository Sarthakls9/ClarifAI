import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

class MetadataParser:
    def __init__(self):
        """
        Initializes the MetadataParser class for web page metadata extraction.
        """
        pass

    def fetch_metadata(self, url: str) -> dict:
        """
        Fetch metadata from a web page.

        Parameters:
        url (str): The URL of the web page.

        Returns:
        dict: Extracted metadata, including title, description, keywords, and Open Graph tags.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            
            metadata = {}

            # Extract title
            title_tag = soup.find("title")
            metadata["title"] = title_tag.text.strip() if title_tag else "No title found"

            # Extract meta description
            description_tag = soup.find("meta", attrs={"name": "description"})
            metadata["description"] = description_tag["content"].strip() if description_tag else "No description found"

            # Extract meta keywords
            keywords_tag = soup.find("meta", attrs={"name": "keywords"})
            metadata["keywords"] = keywords_tag["content"].strip() if keywords_tag else "No keywords found"

            # Extract Open Graph metadata (og:title, og:description)
            metadata["og:title"] = self._get_meta_content(soup, "property", "og:title")
            metadata["og:description"] = self._get_meta_content(soup, "property", "og:description")
            metadata["og:image"] = self._get_meta_content(soup, "property", "og:image")

            return metadata

        except requests.RequestException as e:
            return {"error": f"Failed to fetch metadata: {str(e)}"}

    def _get_meta_content(self, soup, attr_name: str, attr_value: str) -> str:
        """
        Helper function to get the content of a meta tag.

        Parameters:
        soup (BeautifulSoup): The BeautifulSoup object of the web page.
        attr_name (str): The attribute name (e.g., "property").
        attr_value (str): The attribute value to search for (e.g., "og:title").

        Returns:
        str: Content of the meta tag or "Not found".
        """
        tag = soup.find("meta", attrs={attr_name: attr_value})
        return tag["content"].strip() if tag and tag.get("content") else "Not found"
