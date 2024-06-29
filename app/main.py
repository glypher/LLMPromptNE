from typing import Union
from fastapi import FastAPI, Response
from pydantic import BaseModel

from .model import Model


class Prompt(BaseModel):
    text: str


app = FastAPI()

model = Model()

with open('app/static/index.html') as f:
    web_content = f.read()

@app.get("/")
async def web_root():
    return Response(web_content, media_type='html')

@app.post("/v1/protect")
async def create_item(prompt: Prompt):
    return { 'message': model.protect(prompt.text) }

