from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch

class TextToImageAligner:
    def __init__(self, model_name="openai/clip-vit-large-patch14"):
        self.processor = CLIPProcessor.from_pretrained(model_name)
        self.model = CLIPModel.from_pretrained(model_name)

    def align_text_image(self, text: str, image_path: str) -> float:
        image = Image.open(image_path)
        inputs = self.processor(
            text=[text], images=image, return_tensors="pt", padding=True
        )
        outputs = self.model(**inputs)
        logits = outputs.logits_per_image
        return logits.item()
