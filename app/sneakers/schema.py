from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from typing_extensions import Annotated

DESC_EXAMPLE = "The radiance lives on in the Nike Air Force 1 '07, the basketball original that puts a fresh spin on what you know best: durably stitched overlays, clean finishes and the perfect amount of flash to make you shine."


class SneakerSchema(BaseModel):
    brand_name: str = Field(example="Nike")
    name: str = Field(example="Nike Air Force 1 '07")
    description: str = Field(example=DESC_EXAMPLE)
    size: Annotated[int, Field(ge=38, le=53, example=42)]
    color: str = Field(example="White")
    free_delivery: Optional[bool] = Field(default=None, example=False)
