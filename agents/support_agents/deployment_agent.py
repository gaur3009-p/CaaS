import requests

class DeploymentAgent:
    def deploy_to_facebook(self, ad_creative: dict, api_token: str):
        url = "https://graph.facebook.com/v12.0/act_<AD_ACCOUNT_ID>/adcreatives"
        payload = {
            "name": ad_creative["name"],
            "object_story_spec": ad_creative["object_story_spec"],
            "access_token": api_token
        }
        response = requests.post(url, json=payload)
        return response.json()
