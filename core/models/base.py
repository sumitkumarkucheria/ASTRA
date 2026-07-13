from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class AstraMessage(BaseModel):

    message_id: str = Field(default_factory=lambda: str(uuid4()))

    timestamp: datetime = Field(default_factory=datetime.utcnow)

    sender: str

    type: str

    payload: dict
