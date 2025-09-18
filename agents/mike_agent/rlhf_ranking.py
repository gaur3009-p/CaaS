class RLHFRanker:
    def __init__(self):
        self.feedback_history = []

    def rank_creatives(self, creatives: list, feedback_scores: list) -> dict:
        ranked = {creative: score for creative, score in zip(creatives, feedback_scores)}
        return dict(sorted(ranked.items(), key=lambda x: x[1], reverse=True))
