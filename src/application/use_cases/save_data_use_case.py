import datetime
import logging
from domain.use_case import UseCase
from application.dtos.save_data import SaveData
from infrastructure.sqlite.extracted_data_repo import ExtractedDataRepo

logger = logging.getLogger(__name__)

class SaveDataUseCase(UseCase):
    def __init__(self):
        self.repo = ExtractedDataRepo()

    def execute(self, arg: SaveData) -> datetime.datetime:
        logger.info("saving data to database")
        logger.info(arg)
        return self.repo.save_data(arg)
