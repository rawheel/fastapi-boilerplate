import os
import orjson
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv(".env")

Base = declarative_base()


def orjson_serializer(obj):
    """
    Note that `orjson.dumps()` return byte array, while sqlalchemy expects string, thus `decode()` call.
    This function helped to solve JSON datetime conversion issue on JSONB column
    """
    return orjson.dumps(
        obj, option=orjson.OPT_SERIALIZE_NUMPY | orjson.OPT_NAIVE_UTC
    ).decode()


engine = create_engine(
    os.environ["DATABASE_URL"],
    # required for sqlite
    json_serializer=orjson_serializer,
    json_deserializer=orjson.loads,
    connect_args={},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
