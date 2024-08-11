from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse
from typing import List
from io import StringIO
import io
import json
from datetime import datetime
import base64

from backend import Bot
from utils import json_to_ics

app = FastAPI()

@app.post("/image/")
async def image(request: Request):
        body = await request.json()
        base64_image = body.get('image')
        
        if not base64_image:
            raise HTTPException(status_code=400, detail="No image data found")
        
        
        bot = Bot()
        bot_response = bot.ping_ai(base64_image=base64_image)
        date_json = bot_response["choices"][0]["message"]["content"]
        formatted_date = json.dumps(json.loads(date_json), indent=4, sort_keys=True)
        ics_content = json_to_ics(formatted_date)
        ics_file = StringIO(ics_content)

        return StreamingResponse(
            ics_file,
            media_type="text/calendar",
            headers={"Content-Disposition": "attachment; filename=event.ics"}
        )
