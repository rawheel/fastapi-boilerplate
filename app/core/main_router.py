from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/healthcheck", status_code=200)
def healthcheck():
    return JSONResponse(content=jsonable_encoder({"status": "Healthy yayy!"}))
