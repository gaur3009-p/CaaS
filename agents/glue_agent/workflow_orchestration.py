from langchain.chains import SequentialChain
from linda_chain import LindaChain
from mike_chain import MikeChain

class WorkflowOrchestrator:
    def __init__(self):
        self.linda_chain = LindaChain()
        self.mike_chain = MikeChain()

    def run_workflow(self, brand_guidelines: str, feedback_text: str) -> dict:
        creative = self.linda_chain.generate_creative(brand_guidelines)

        analysis = self.mike_chain.analyze_creative(creative, feedback_text)

        return {
            "creative": creative,
            "analysis": analysis
        }
