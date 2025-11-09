from pydantic import BaseModel
from typing import List

class ProductRequirement(BaseModel):
    product_type: str
    expected_users: int
    region: str
    database_preference: str
    other_requirements: List[str] = []
