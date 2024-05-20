from typing import Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import random
import time


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
    img['width'] = 500
    img['height'] = 500
    img['rects'] = []
    for _ in range(rect_cnt):
        img['rects'].append(randomRect(img['width'], img['height']))
    return img


app = FastAPI()


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to be more restrictive in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/randomimg")
async def randomImg():
    resp_type = random.randint(0, 10)
    if resp_type == 0:
        time.sleep(4)
        return generateImg(random.randint(10, 20))
    elif resp_type == 1:
        raise HTTPException(status_code=500, detail="random server error")
    elif resp_type == 2:
        return generateImg(random.randint(10, 20) * 10000)
    
    return generateImg(random.randint(10, 20))

