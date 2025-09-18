from langchain.chains import LLMChain, TransformChain, SequentialChain
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from agents.mike_agent.sentiment_analyzer import SentimentAnalyzer
from agents.mike_agent.engagement_predictor import EngagementPredictor
from agents.mike_agent.rlhf_ranking import RLHFRanker

class MikeChain:
    def __init__(self):
        self.sentiment_analyzer = SentimentAnalyzer()

        self.engagement_predictor = EngagementPredictor()

        self.ranker = RLHFRanker()

    def analyze_creative(self, creative: dict, feedback_text: str) -> dict:
        sentiment_score = self.sentiment_analyzer.analyze_feedback(
            feedback_text,
            creative["ad_copy"]
        )

        engagement_forecast = self.engagement_predictor.predict_engagement(
            historical_data=pd.DataFrame({
                "ds": pd.date_range(start="2023-01-01", periods=10),
                "y": [random.randint(100, 500) for _ in range(10)]
            })
        )

        ranked_creatives = self.ranker.rank_creatives(
            creatives=[creative["ad_copy"]],
            feedback_scores=[sentiment_score]
        )

        return {
            "sentiment_score": sentiment_score,
            "engagement_forecast": engagement_forecast.to_dict(),
            "ranked_creatives": ranked_creatives
        }
