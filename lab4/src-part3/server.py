from typing import Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Form, HTTPException, WebSocket
# from fastapi.middleware.cors import CORSMiddleware
import random
import datetime, time
import json


# interface Rect {
#     x: number;
#     y: number;
#     width: number;
#     height: number;
#     color: string;
# }


def randomRect(width, height):
    rect = {}
    rect['x'] = random.randint(0, width - 10)
    rect['y'] = random.randint(0, height - 10)
    rect['width'] = random.randint(10, width - rect['x'])
    rect['height'] = random.randint(10, height - rect['y'])
    rect['color'] = "#" + "%06x" % random.randint(0, 0xFFFFFF)
    return rect

def generateImg(rect_cnt):
    img = {}
    img['width'] = 70
    img['height'] = 70
    img['rects'] = []
    img['data'] = str(datetime.datetime.now().time())
    for _ in range(rect_cnt):
        img['rects'].append(randomRect(img['width'], img['height']))
    return img


app = FastAPI()


import asyncio

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    _ = await websocket.receive_text()
    while True:
        await asyncio.sleep(1)  # Asynchronous delay
        print("sending")
        await websocket.send_text(json.dumps(generateImg(random.randint(10, 20))))



