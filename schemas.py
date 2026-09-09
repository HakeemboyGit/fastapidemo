from pydantic import BaseModel
from decimal import Decimal
from datetime import date

# Base properties
class CategoryBase(BaseModel):
    name	: str
    description	: str
    status	: bool
    created_at	: date
    category_image :str

# Schema for client responses (Read)
class CategoryResponse(CategoryBase):
    id : int
    name	: str
    description	: str
    status	: bool
    created_at	: date
    category_image :str

    class Config:
        from_attributes = True  # Allows Pydantic to read SQLAlchemy ORM objects
