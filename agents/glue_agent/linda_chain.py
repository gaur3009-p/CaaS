from langchain.chains import LLMChain, TransformChain, SequentialChain
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from agents.linda_agent.ad_copy_generator import AdCopyGenerator
from agents.linda_agent.image_generator import ImageGenerator
from agents.linda_agent.text_to_image_aligner import TextToImageAligner

class LindaChain:
    def __init__(self):
        self.ad_copy_template = PromptTemplate(
            input_variables=["brand_guidelines"],
            template="Generate an engaging ad copy for: {brand_guidelines}"
        )
        self.ad_copy_llm = HuggingFaceHub(
            repo_id="facebook/bart-large-cnn",
            model_kwargs={"temperature": 0.7, "max_length": 100}
        )
        self.ad_copy_chain = LLMChain(
            llm=self.ad_copy_llm,
            prompt=self.ad_copy_template,
            output_key="ad_copy"
        )

        self.image_generator = ImageGenerator()

        self.aligner = TextToImageAligner()

    def generate_creative(self, brand_guidelines: str) -> dict:
        ad_copy = self.ad_copy_chain.run(brand_guidelines)

        image_path = self.image_generator.generate_image(ad_copy)

        alignment_score = self.aligner.align_text_image(ad_copy, image_path)

        return {
            "ad_copy": ad_copy,
            "image_path": image_path,
            "alignment_score": alignment_score
        }
