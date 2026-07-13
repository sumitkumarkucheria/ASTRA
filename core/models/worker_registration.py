from __future__ import annotations

from pydantic import BaseModel


class WorkerRegistration(BaseModel):

    worker_id: str

    hostname: str

    ip_address: str

    platform: str

    python_version: str

    cpu_cores: int

    logical_threads: int

    ram_total_mb: int

    slots: int

    astra_version: str
