from typing import Union

from fastapi import FastAPI

from algorithm_api.routers import search

app = FastAPI()
app.include_router(search)


@app.get("/")
async def read_root():
    return {"Hello": "World"}
