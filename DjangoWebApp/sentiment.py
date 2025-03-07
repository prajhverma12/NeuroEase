from transformers import pipeline

# Load sentiment analysis model (multilingual support)
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_sentiment(text):
    """Analyze sentiment and return Positive, Negative, or Neutral."""
    result = sentiment_pipeline(text)[0]  # Get first prediction
    label = result["label"]

    # Convert the model's label to human-friendly sentiment
    if "1 star" in label or "2 stars" in label:
        return "Negative"
    elif "4 stars" in label or "5 stars" in label:
        return "Positive"
    else:
        return "Neutral"
