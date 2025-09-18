from utils.models import load_bart_summarizer, load_gpt_neo_generator, load_stable_diffusion

class LindaAgent:
    def __init__(self):
        self.ad_copy_summarizer = load_bart_summarizer()
        self.ad_script_generator = load_gpt_neo_generator()
        self.poster_designer = load_stable_diffusion()

    def generate_ad_copy(self, brand_guideline):
        return self.ad_copy_summarizer(brand_guideline, max_length=130, min_length=30, do_sample=False)

    def generate_ad_script(self, prompt):
        return self.ad_script_generator(prompt, max_length=200, num_return_sequences=3)

    def generate_poster(self, prompt):
        return self.poster_designer(prompt).images[0]
