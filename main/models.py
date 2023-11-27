from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum


class OsType(str, Enum):
    Android = "Android"
    iOS = "iOS"
    Windows = "Windows"
    Other = "Other"

class MobilePhone(BaseModel):
    Id: Optional[int] = Field(default=None, description="Optional ID. If not provided, it will be assigned automatically.")
    Name: str
    Brand: str
    Release: int
    OS: OsType
    
