import uvicorn
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/")
async def read_items():
    return {'hello': 'world'}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")