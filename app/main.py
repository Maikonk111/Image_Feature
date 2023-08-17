import cv2
import numpy as np
import base64
from app.hog import getHog_descriptors
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def readb64(item_str):
    encode_data = item_str.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encode_data),np.uint8)
    img = cv2.imdecode(nparr,cv2.IMREAD_GRAYSCALE)
    return img

@app.get("/")
def root():
    return {"message": "This is my APIS"}

@app.get("/api/gethog")
async def get_hot_with_input_data(request:Request):  # Expecting base64-encoded image as a query parameter
    try:
        item =  await request.json()
        item_str = item['img']
        img = readb64(item_str)
        hog = getHog_descriptors(img)
        return {"Hog": hog.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

