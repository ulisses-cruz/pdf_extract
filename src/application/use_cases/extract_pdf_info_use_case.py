import io
import re
import logging
from google import genai

from settings import Settings
from domain.use_case import UseCase
from application.dtos.extracted_info import ExtractedInfo

logger = logging.getLogger(__name__)

class ExtractPDFInfoUseCase(UseCase):
    def execute(self, arg: io.BytesIO) -> ExtractedInfo:
        logger.info("extracting info from file")

        client = genai.Client(api_key=Settings.GEMINI_API_KEY)
        logger.info("connected to gemini API")

        logger.info("uploading pdf to gemini")
        sample_doc = client.files.upload(
            file=arg,
            config={"mime_type": "application/pdf"}
        )

        prompt="""
            extrair os seguintes campos do documento jurídico:
            - resume: um pequeno texto com um sumário do documento;
            - timeline: uma lista de eventos referidos no documento;
            - evidence: uma lista de evidencias referidas no documento;

            cada evento da `timeline` terá os seguintes campos:
            - event_id: será um número que identifica o evento;
            - event_name: texto com o nome do evento;
            - event_description: texto com uma descrição do evento;
            - event_date: texto a data do evento no seguinte formato `AAAA-MM-DD` (onde DD=dia <número> , MM=mês <número> e AAAA=ano <número>);
            - event_page_init: número da página onde o evento começa no documento pdf;
            - event_page_end: número da página onde o evento termina no documento pdf;
            Não retorne eventos com `event_date` inválida, está só deve ser composto por digitos e o hifen '-'

            cada item da lista `evidence` terá os seguintes campos:
            - evidence_id: número que identifica a evidência;
            - evidence_name: texto com o nome da evidência;
            - evidence_flaw: texto identificando alguma inconcistência na evidência, caso não exista retorne aqui o texto "Sem inconsistências";
            - evidence_page_init: número da página onde a evidência começa no documento pdf;
            - evidence_page_end: número da página onde a evidência termina no documento pdf;

            Deve retornar as informações extraídas em formato JSON.
            Deve retornar apenas os campos pedidos.
            """

        logger.info("requesting info from gemini")
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[sample_doc, prompt] 
        )
        pattern = re.compile(r'```json\n((?:.|\n)*)\n```', re.MULTILINE)
        match = pattern.match(str(response.text))
        if not match: 
            raise Exception('could not extract information from pdf')

        res_data = match.group(1)
        info = ExtractedInfo.model_validate_json(json_data=res_data)
        return info
