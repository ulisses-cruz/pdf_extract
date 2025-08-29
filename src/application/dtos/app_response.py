from datetime import datetime

from application.dtos.extracted_info import ExtractedInfo


class AppResponse(ExtractedInfo):
    case_id: str
    persisted_at: datetime
