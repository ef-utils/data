import json
from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

f = open('data.json')
data = json.load(f)
f.close()

@app.get('/')
async def root():
    return data