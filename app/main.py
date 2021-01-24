from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.params import Header
from linebot.exceptions import InvalidSignatureError
from starlette.requests import Request
from starlette.status import HTTP_200_OK

from app.event_handler import handler

router = FastAPI()


@router.post("/webhook")
async def webhook_handler(request: Request):
    """
    Handle all webhook requests from LINE
    """

    body = await request.body()
    sign = request.headers["x-line-signature"]
    try:
        handler.handle(body.decode(), sign)
    except InvalidSignatureError:
        err = (
            f"Invalid Signature, check token and secret\n"
            f"request body:\n"
            f"{body.decode()}"
        )
        print(err)
        raise HTTPException(HTTP_200_OK, detail=err)
    else:
        return "OK"
