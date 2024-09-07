from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from getData import *

app = FastAPI()

origins = ['http://localhost:3000', 'https://localhost:3000','*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/event_list")
async def eventList():
    return getEventList()

@app.get("/id={event_id}")
async def eventInfo(event_id):
    return getEventInfo(event_id)

@app.get("/roomList={event_id}")
async def roomList(event_id):
    return getRoomList(event_id)

@app.get("/roomInfo={event_id}&{room_id}")
async def roomInfo(event_id,room_id):
    return getRoomInfo(event_id,room_id)
