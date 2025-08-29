import io
import requests
import logging
from pydantic import HttpUrl

from src.domain.use_case import UseCase

logger = logging.getLogger(__name__)

class DownloadPDFUseCase(UseCase):
    def execute(self, arg: HttpUrl) -> io.BytesIO:
        logger.info("downloading file", arg)
        response = requests.get(arg.encoded_string())
        return io.BytesIO(response.content)

