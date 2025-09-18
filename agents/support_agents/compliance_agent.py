from transformers import pipeline

class ComplianceAgent:
    def __init__(self, model_name="roberta-base-mnli"):
        self.classifier = pipeline("zero-shot-classification", model=model_name)

    def check_compliance(self, ad_copy: str, policies: list) -> bool:
        result = self.classifier(ad_copy, policies)
        return all(score > 0.7 for score in result["scores"])
