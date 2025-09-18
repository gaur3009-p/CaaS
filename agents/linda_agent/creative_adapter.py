from transformers import AutoModelForSequenceClassification, AutoTokenizer

class CreativeAdapter:
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)

    def adapt_tone(self, text: str, target_tone: str) -> str:
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model(**inputs)
        predicted_tone = "positive" if outputs.logits.argmax().item() == 1 else "negative"
        if predicted_tone != target_tone:
            return f"Adapted {text} to {target_tone} tone."
        return text
