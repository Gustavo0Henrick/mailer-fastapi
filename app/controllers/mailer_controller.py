from fastapi import APIRouter
from app.models.email_request_model import EmailRequest
from fastapi_mailman import EmailMessage, Mail
from starlette.responses import JSONResponse
from app.config.email_config import config


router = APIRouter()


mail = Mail(config)
headerHtml = """Thanks for using Fastapi-mail"""
title = "Email FastAPI"
body = "Hello World"


@router.post('/sendEmail')
async def send_email(emailRespose: EmailRequest) -> JSONResponse:
    msg = EmailMessage(
        headerHtml,
        body,
        title,
        [emailRespose.email],
    )
    await msg.send()
    return JSONResponse(status_code=200, content={"message": f"email has been sent to {emailRespose.email}"})
