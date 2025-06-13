from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    name: str
    price: float
    # description: str | None = None
    # description: Optional[str] = None
    image: str
