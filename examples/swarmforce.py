import requests
from config import SWARMFORCE_URL
from pydantic import BaseModel
from typing import List, Union, Generator, Iterator

class Pipeline:
    def __init__(self):
        self.name = "SwarmForce"

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
    ) -> Union[str, Generator, Iterator]:
        print(f"Running command for user message: '{user_message}'")
        platform = body["platform"]
        try:
            response = requests.post(
                f"{SWARMFORCE_URL}/api/commands.run",
                json={
                    "id": platform["id"],
                    "prompt": user_message
                },
                headers={
                    "Authorization": f"Bearer {platform["key"]}"
                }
            )
            body = response.json()
            return body["result"]["data"]
        except:
            return "Failed to process response. Try again later!"
