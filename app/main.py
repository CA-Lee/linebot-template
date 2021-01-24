from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.params import Header
from linebot.exceptions import InvalidSignatureError
from starlette.requests import Request
from starlette.status import HTTP_200_OK

from app.event_handler import handler

router = FastAPI()


@router.post("/webhook")
async def webhook_handler(
    request: Request, sign: str = Header("", alias="x-line-signature")
):
    """
    Handle all webhook requests from LINE
    """

    try:
        handler.handle((await request.body()).decode(), sign)
    except InvalidSignatureError:
        err = (
            f"Invalid Signature, check token and secret\n"
            f"request body:\n"
            f"{(await request.body()).decode()}"
        )
        print(err)
        raise HTTPException(HTTP_200_OK, detail=err)
    else:
        return "OK"
