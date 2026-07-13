from __future__ import annotations

from pydantic import BaseModel

from core.models.worker_registration import WorkerRegistration
from core.models.worker_runtime import WorkerRuntime


class Worker(BaseModel):

    registration: WorkerRegistration

    runtime: WorkerRuntime 
