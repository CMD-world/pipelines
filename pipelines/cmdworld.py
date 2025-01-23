import json
import requests
from config import CMDWORLD_URL
from typing import List, Union, Generator, Iterator

class Pipeline:
    def __init__(self):
        self.name = "CMD.world"

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
    ) -> Union[str, Generator, Iterator]:
        print(f"Running command for user message: '{user_message}'")
        platform = body.get("platform")
        if not (platform and platform.get("id") and platform.get("key")):
            return "Chat must be linked to a command to use CMD.world. Go to CMD.world and start new chat there!"
        print(f"Got platform: {platform}")

        try:
            # Get SSE connection
            response = requests.get(
                f"{CMDWORLD_URL}/api/run",
                params={
                    "id": platform["id"],
                    "prompt": user_message
                },
                headers={
                    "Authorization": f"Bearer {platform['key']}",
                    "Accept": "text/event-stream"
                },
                stream=True
            )
            response.raise_for_status()

            # Parse each chunk and return
            for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
                if chunk:
                    try:
                        data = json.loads(chunk.replace("data: ", ""))
                        if "content" in data:
                            yield data["content"]
                    except json.JSONDecodeError:
                        continue
        except:
            return "Failed to process response. Try again later!"
