from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class AdCopyGenerator:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def generate_ad_copy(self, brand_guidelines: str, max_length: int = 100) -> str:
        inputs = self.tokenizer(brand_guidelines, return_tensors="pt", truncation=True, max_length=512)
        outputs = self.model.generate(**inputs, max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
