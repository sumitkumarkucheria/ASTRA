from fastapi import FastAPI

from core.common.logger import get_logger
from core.config.loader import load_config

logger = get_logger("master")

config = load_config("configs/master.yaml")

app = FastAPI(
    title="ASTRA Master",
    version="0.1.0",
)

logger.info("Master started")


@app.get("/")
def root():

    return {
        "project": "ASTRA",
        "version": "0.1.0",
        "status": "running",
    }
