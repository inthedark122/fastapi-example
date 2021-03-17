import logging
from typing import Optional, Any, Type
from fastapi_example.api.api_v1.api import api_router
from pydantic.error_wrappers import ValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status
from init import app

logger = logging.getLogger(__name__)

app.include_router(api_router, prefix="/api/v1")


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Any, exc: Any) -> Any:
    logger.info("ValidationError: {errors}".format(errors=exc.errors()))
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"detail": exc.errors()})
    )