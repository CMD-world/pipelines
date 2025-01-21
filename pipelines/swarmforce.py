import requests
from config import SWARMFORCE_URL
from typing import List, Union, Generator, Iterator

class Pipeline:
    def __init__(self):
        self.name = "SwarmForce"

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
    ) -> Union[str, Generator, Iterator]:
        print(f"Running command for user message: '{user_message}'")
        platform = body.get("platform")
        if not (platform and platform.get("id") and platform.get("key")):
            return "Chat must be linked to a command to use SwarmForce. Go to swarmforce.com and start new chat there!"
        print(f"Got platform: {platform}")

        try:
            response = requests.post(
                f"{SWARMFORCE_URL}/api/commands.run",
                json={
                    "id": platform["id"],
                    "prompt": user_message
                },
                headers={
                    "Authorization": f"Bearer {platform['key']}"
                }
            )
            body = response.json()
            return body["result"]["data"]
        except:
            return "Failed to process response. Try again later!"
