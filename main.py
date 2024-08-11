from backend import Bot
from utils import json_to_ics

import json
from datetime import datetime


if __name__ == "__main__":
    bot = Bot()
    bot_response = bot.ping_ai("img.png")
    date_json = bot_response["choices"][0]["message"]["content"]

    formatted_date = json.dumps(json.loads(date_json), indent=4, sort_keys=True)
    json_to_ics(formatted_date)





