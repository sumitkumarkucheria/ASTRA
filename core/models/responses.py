from __future__ import annotations

from pydantic import BaseModel


class RegistrationResponse(BaseModel):
    accepted: bool
    worker: str
    message: str


class ErrorResponse(BaseModel):
    error: str
    detail: str
