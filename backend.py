import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

class Bot:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.system_prompt = "return the name, time, location into json"
        self.prompt = "return the name, time, location into json"

    def encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def ping_ai(self, base64_image):

        headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": f"{self.system_prompt}"
                    },
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"{self.prompt}"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
            "name": "events_response",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                "events": {
                    "type": "array",
                    "items": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "time": {
                            "type": "string"
                        },
                        "location": {
                            "type": "string"
                        },
                        
                    },
                    "required": ["name", "time", "location"],
                    "additionalProperties": False
                    }
                }
                },
                "required": ["events"],
                "additionalProperties": False
            }
            }
        },
        "max_tokens": 300
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

        return response.json()