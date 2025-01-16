import requests
from pydantic import BaseModel
from typing import List, Union, Generator, Iterator

class Pipeline:
    class Valves(BaseModel):
        api_key: str = ""
        command: str = ""

    def __init__(self):
        self.name = "cmd.world"

        # Initialize valves
        self.valves = self.Valves(
            **{
                "api_key": "",
                "command": ""
            }
        )

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
    ) -> Union[str, Generator, Iterator]:
        response = requests.post(
            "http://localhost:5174/api/commands.run",
            json={
                "slug": self.valves.command,
                "prompt": user_message
            },
            headers={
                "Authorization": f"Bearer {self.valves.api_key}"
            }
        )
        return response.json()["result"]["data"]
