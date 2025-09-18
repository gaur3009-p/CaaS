from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class SentimentAnalyzer:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def analyze_feedback(self, feedback_text: str, reference_text: str) -> float:
        embeddings = self.model.encode([feedback_text, reference_text])
        return cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
