from domain.use_case import UseCase
from application.dtos.save_data import SaveData
from application.dtos.app_request import AppRequest
from application.dtos.app_response import AppResponse
from application.use_cases.save_data_use_case import SaveDataUseCase
from application.use_cases.download_pdf_use_case import DownloadPDFUseCase
from application.use_cases.extract_pdf_info_use_case import ExtractPDFInfoUseCase


class AppUseCase(UseCase):

    def execute(self, arg: AppRequest) -> AppResponse: 
        doc = DownloadPDFUseCase().execute(arg.pdf_url)
        info = ExtractPDFInfoUseCase().execute(doc)
        save_data = SaveData(
            case_id=arg.case_id,
            pdf_url=arg.pdf_url,
            data=info.model_dump_json()
        )
        persisted_at = SaveDataUseCase().execute(save_data)

        return AppResponse(
            case_id = arg.case_id,
            resume = info.resume,
            timeline = info.timeline,
            evidence = info.evidence,
            persisted_at=persisted_at
        )
