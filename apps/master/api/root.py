from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():

    return {

        "project": "ASTRA",

        "version": "0.1.0",

        "status": "running"

    }
