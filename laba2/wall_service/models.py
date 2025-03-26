from pydantic import BaseModel
from datetime import datetime,timezone

class WallPost(BaseModel):
    id: int
    content: str
    author: str
    created_at: datetime = datetime.now(timezone.utc)
