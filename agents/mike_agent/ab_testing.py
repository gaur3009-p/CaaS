import random

class ABTesting:
    def __init__(self):
        self.results = {}

    def run_test(self, creative_a: str, creative_b: str, audience_size: int = 1000) -> dict:
        self.results = {
            "creative_a": {"impressions": audience_size // 2, "ctr": random.uniform(0.01, 0.1)},
            "creative_b": {"impressions": audience_size // 2, "ctr": random.uniform(0.01, 0.1)},
        }
        return self.results
