from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class WallPost(BaseModel):
    id: Optional[str] = None
    content: str
    author: str
    created_at: Optional[datetime] = None