from typing import Union

from fastapi import FastAPI
from fastapi import Response


app = FastAPI()

with open('app/static/index.html') as f:
    web_content = f.read()

@app.get("/")
async def web_root():
    return Response(web_content, media_type='html')

