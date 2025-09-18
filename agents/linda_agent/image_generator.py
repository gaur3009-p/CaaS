from diffusers import StableDiffusionXLPipeline
import torch

class ImageGenerator:
    def __init__(self, model_name="stabilityai/stable-diffusion-xl-base-1.0"):
        self.pipe = StableDiffusionXLPipeline.from_pretrained(
            model_name, torch_dtype=torch.float16, use_safetensors=True
        ).to("cuda" if torch.cuda.is_available() else "cpu")

    def generate_image(self, prompt: str, output_path: str = "output.png"):
        image = self.pipe(prompt).images[0]
        image.save(output_path)
        return output_path
