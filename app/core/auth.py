import os
from dotenv import load_dotenv
from fastapi import Header, HTTPException

load_dotenv(".env")

X_TOKEN = os.environ["X_TOKEN"]


async def verify_token(x_token: str = Header()):
    if x_token != X_TOKEN:
        raise HTTPException(status_code=400, detail="X-Token header invalid")
