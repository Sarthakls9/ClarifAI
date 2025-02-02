from transformers import pipeline

# Initialize NLP Models for Text Analysis
sentiment_pipeline = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
fact_check_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def analyze_text(text_data):
    """
    Analyze the text for misinformation and return a trust score using Hugging Face models.
    """
    try:
        # Analyze sentiment for potentially inflammatory or fake tone
        sentiment_result = sentiment_pipeline(text_data)[0]
        sentiment_label = sentiment_result['label']
        sentiment_score = sentiment_result['score']

        # Sentiment trust assessment
        if sentiment_label == 'NEGATIVE':
            sentiment_score = 50 - int(sentiment_score * 50)  # Penalize negative tone
        else:
            sentiment_score = 70 + int(sentiment_score * 30)  # Reward positive tone

        # Fact-checking using Hugging Face QA model
        fact_check_context = """
        The moon landing was real and occurred in 1969 when NASA's Apollo 11 mission successfully landed astronauts 
        on the moon. Vaccines are scientifically proven to be effective and safe in preventing diseases.
        Climate change is real and is driven by human activities, according to scientific consensus.
        """
        question = f"Is it true: '{text_data}'?"
        fact_check_result = fact_check_pipeline(question=question, context=fact_check_context)

        # Fact-check trust assessment
        if fact_check_result['score'] > 0.7:
            fact_check_score = 90
        else:
            fact_check_score = 50

        # Calculate a combined trust score
        combined_score = (sentiment_score + fact_check_score) // 2

        return {
            "trust_score": combined_score,
            "details": f"Sentiment Trust: {sentiment_score}. Fact Check Trust: {fact_check_score}."
        }

    except Exception as e:
        return {"trust_score": 0, "details": f"Text analysis failed: {str(e)}"}
