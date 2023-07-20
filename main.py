from fastapi import FastAPI

from schemas import Url

app = FastAPI()


@app.post("/encode")
def encode(
    url: Url,
) -> Url:
    return url
