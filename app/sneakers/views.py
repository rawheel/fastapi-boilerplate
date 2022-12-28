from loguru import logger
from fastapi import Depends, APIRouter, HTTPException, Body
from app.core.auth import verify_token


router = APIRouter(dependencies=[Depends(verify_token)])


@router.get("/sneakers")
async def sneakers():
    return "yes sneakersss nooooo"
