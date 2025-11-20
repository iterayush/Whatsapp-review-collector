from pydantic import BaseModel
from datetime import datetime

class ReviewOut(BaseModel):
    id: int
    contact_number: str
    user_name: str | None = None
    product_name: str | None = None
    product_review: str | None = None
    created_at: datetime

    class Config:
        orm_mode = True
