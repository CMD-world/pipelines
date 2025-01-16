from typing import List, Union, Generator, Iterator
from schemas import OpenAIChatMessage
from pydantic import BaseModel
import subprocess


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
        return user_message
