import logging
from fastapi import FastAPI
from fastapi_example.core.config import settings

app = FastAPI(
    description=settings.description
)


@app.on_event("startup")
async def startup_event() -> None:
    root_logger = logging.getLogger()
    app_logger = logging.getLogger("fastapi_example")
    main_logger = logging.getLogger("main")
    handler = logging.StreamHandler()

    root_logger.setLevel(logging.INFO)

    handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
    main_logger.addHandler(handler)
    app_logger.addHandler(handler)