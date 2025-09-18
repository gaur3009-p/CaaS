from transformers import pipeline

class PersonaAgent:
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        self.sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)

    def extract_brand_tone(self, brand_guidelines: str) -> str:
        result = self.sentiment_analyzer(brand_guidelines)[0]
        return result["label"]
