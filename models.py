from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: float
    on_offer: bool = False
