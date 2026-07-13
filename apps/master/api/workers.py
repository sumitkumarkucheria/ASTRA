from fastapi import APIRouter

from core.models.worker import Worker

from apps.master.services.worker_registry import registry

router = APIRouter(prefix="/api/v1/workers", tags=["Workers"])


from fastapi import status

from core.models.responses import RegistrationResponse
@router.post(
    "/register",
    response_model=RegistrationResponse,
    status_code=status.HTTP_201_CREATED,
)

def register(worker: Worker):

    registry.register(worker)

    return RegistrationResponse(
    accepted=True,
    worker=worker.registration.worker_id,
    message="Worker successfully registered."
)


@router.get("/")
def list_workers():
    return {
    "count": len(registry.all()),
    "workers": registry.all() }
