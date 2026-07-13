from fastapi import FastAPI

from core.common.logger import get_logger

from core.config.loader import load_config

from apps.master.api.root import router as root_router

from apps.master.api.workers import router as worker_router

logger = get_logger("master")

config = load_config("configs/master.yaml")

app = FastAPI(

    title="ASTRA Master",

    version="0.1.0",
    description="""ASTRA Distributed Computing Platform
                        Master Node API Version 0.1.0  """

)

app.include_router(root_router)

app.include_router(worker_router)

logger.info("Master started")
