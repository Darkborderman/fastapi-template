from fastapi.responses import PlainTextResponse
from loguru import logger
# pylint: disable=E0611
from pydantic import BaseModel

from memory import FRUIT

# pylint: enable=E0611


DOC = {
    200: {
        "description": "API response successfully",
        "content": {"application/json": {"example": "OK"}},
    },
    400: {
        "description": "API response successfully",
        "content": {"text/plain": {"example": "Bad Request"}},
    },
}


class Payload(BaseModel):
    name: str
    count: int = 0


def post(payload: Payload):
    try:
        if payload.name in FRUIT:
            raise Exception(f"Fruit {payload.name} already exists!")
        FRUIT[payload.name] = payload.count
        return PlainTextResponse("OK", 200)
    except Exception as error:
        logger.warning(error)
        return PlainTextResponse("Bad Request", 400)
