from pinecone import Pinecone

class MemoryManager:
    def __init__(self, api_key: str, index_name: str = "campaign-memory"):
        self.pinecone = Pinecone(api_key=api_key)
        self.index = self.pinecone.Index(index_name)

    def store_campaign(self, campaign_id: str, data: dict):
        self.index.upsert([{"id": campaign_id, "values": data}])

    def retrieve_campaign(self, campaign_id: str) -> dict:
        result = self.index.fetch(ids=[campaign_id])
        return result["vectors"][campaign_id]["values"]
