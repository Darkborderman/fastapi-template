from fastapi.responses import JSONResponse, PlainTextResponse
from loguru import logger

from memory import FRUIT

# Basic example for using params and headers
DOC = {
    200: {
        "description": "API response successfully",
        "content": {"application/json": {"example": {"name": "apple"}}},
    },
    400: {
        "description": "API response successfully",
        "content": {"text/plain": {"example": "Bad Request"}},
    },
}


def get_url(name: str):
    try:
        if name not in FRUIT:
            raise Exception(f"Fruit {name} does not exist!")
        return JSONResponse({"name": name, "count": FRUIT[name]}, 200)
    except Exception as error:
        logger.warning(error)
        return PlainTextResponse("Bad Request", 400)
