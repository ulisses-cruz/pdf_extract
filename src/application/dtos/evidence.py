from pydantic import BaseModel


class Evidence(BaseModel):
    evidence_id: int
    evidence_name: str
    evidence_flaw: str | None
    evidence_page_init: int
    evidence_page_end: int
