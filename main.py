from fastapi import Depends, FastAPI, HTTPException, Query, Response
from typing import List
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from model.controller.input.text_request import TextRequest
from common.utils.genid import gen_short_id
from db.client import db_client

app = FastAPI(
    title="pastelueyo",
    description="API para transmitir texto copiado y pegado entre diferentes dispositivos.",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

texts_collection = db_client.texts

# redirect to https://paste.lueyo.es/
@app.get("/")
async def root():
    return RedirectResponse(url="https://paste.lueyo.es/")

@app.get("/ping")
async def ping():
    return {"message": "pong!"}

@app.post("/text")
async def create_text(text_request: TextRequest):
    text_id = gen_short_id()
    timestamp = datetime.now().isoformat()
    document = {
        "_id": text_id,
        "text": text_request.text,
        "timestamp": timestamp
    }
    await texts_collection.insert_one(document)
    return {"id": text_id}

@app.get("/{text_id}")
async def get_text(text_id: str, type: str = Query("txt", enum=["txt", "json"])):
    document = await texts_collection.find_one({"_id": text_id})
    if not document:
        raise HTTPException(status_code=404, detail="Text not found")
    if type == "txt":
        return Response(content=document["text"], media_type="text/plain")
    elif type == "json":
        return {
            "id": document["_id"],
            "text": document["text"],
            "date": document["timestamp"]
        }
