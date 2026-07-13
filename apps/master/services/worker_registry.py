from __future__ import annotations

from typing import Dict

from core.models.worker import Worker


class WorkerRegistry:

    def __init__(self) -> None:

        self._workers: Dict[str, Worker] = {}

    def register(self, worker: Worker) -> None:

        self._workers[worker.registration.worker_id] = worker

    def get(self, worker_id: str):

        return self._workers.get(worker_id)

    def all(self):

        return list(self._workers.values())

    def remove(self, worker_id: str):

        self._workers.pop(worker_id, None)


registry = WorkerRegistry()
