class ScoreCalculator:
    def __init__(self):
        """
        Initialize the scoring system with weights for text, image, and link analysis.
        """
        # Define weights for each input type; these can be adjusted based on requirements
        self.text_weight = 0.4
        self.image_weight = 0.3
        self.link_weight = 0.3

    def calculate_overall_score(self, text_score: int = None, image_score: int = None, link_score: int = None) -> dict:
        """
        Calculate the overall trust score based on provided scores.

        Parameters:
        text_score (int): Trust score from text analysis (0-100)
        image_score (int): Trust score from image analysis (0-100)
        link_score (int): Trust score from link analysis (0-100)

        Returns:
        dict: Final trust score and component breakdown.
        """
        # Initialize component scores
        total_weight = 0.0
        weighted_score = 0.0
        component_scores = {}

        # Include text analysis if score is provided
        if text_score is not None:
            component_scores["text_score"] = text_score
            weighted_score += text_score * self.text_weight
            total_weight += self.text_weight

        # Include image analysis if score is provided
        if image_score is not None:
            component_scores["image_score"] = image_score
            weighted_score += image_score * self.image_weight
            total_weight += self.image_weight

        # Include link analysis if score is provided
        if link_score is not None:
            component_scores["link_score"] = link_score
            weighted_score += link_score * self.link_weight
            total_weight += self.link_weight

        # Calculate the final score
        overall_score = int(weighted_score / total_weight) if total_weight > 0 else 0

        return {
            "overall_trust_score": overall_score,
            "component_scores": component_scores
        }

    def interpret_score(self, score: int) -> str:
        """
        Provide a human-readable interpretation of the trust score.

        Parameters:
        score (int): Trust score (0-100)

        Returns:
        str: Interpretation of the trust score.
        """
        if score >= 80:
            return "Highly Trustworthy"
        elif score >= 50:
            return "Moderately Trustworthy"
        elif score >= 20:
            return "Potentially Untrustworthy"
        else:
            return "Highly Untrustworthy"
