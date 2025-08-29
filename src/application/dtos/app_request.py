from pydantic import HttpUrl, BaseModel

class AppRequest(BaseModel):
    pdf_url: HttpUrl
    case_id: str
