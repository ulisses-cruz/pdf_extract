import logging
from typing import Any

from application.dtos.app_request import AppRequest
from application.dtos.app_response import AppResponse
from application.use_cases.app_use_case import AppUseCase

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def lambda_handler(event: dict[str, Any], context: Any) -> AppResponse:
    valid_event = AppRequest.model_validate(event)
    logger.info("received event", valid_event)
    return AppUseCase().execute(valid_event)

if __name__ == "__main__":
    res = lambda_handler({
        "pdf_url": "http://localhost:8000/0809090-86.2024.8.12.0021.pdf",
        "case_id": "0809090-86.2024.8.12.0021"
    }, None)
    print(AppResponse.model_dump_json(res))
