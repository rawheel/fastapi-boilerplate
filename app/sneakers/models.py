from sqlalchemy import Column, Integer, DateTime, String, Boolean
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.sql import func
from app.core.db.session import Base


class Sneaker(Base):
    __tablename__ = "sneaker"
    id = Column(Integer, primary_key=True)
    brand_name = Column(String, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    size = Column(Integer, index=True)
    color = Column(String, index=True)
    free_delivery = Column(Boolean, index=True)

    class Config:
        orm_mode = True
