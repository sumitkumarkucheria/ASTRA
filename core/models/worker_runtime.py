from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class WorkerRuntime(BaseModel):

    status: str = "ONLINE"

    score: float = 100

    cpu_percent: float = 0

    ram_percent: float = 0

    current_jobs: int = 0

    last_heartbeat: datetime = Field(default_factory=datetime.utcnow)
