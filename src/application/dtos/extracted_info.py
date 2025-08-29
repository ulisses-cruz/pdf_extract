from pydantic import BaseModel

from src.application.dtos.evidence import Evidence
from src.application.dtos.timeline_event import TimelineEvent


class ExtractedInfo(BaseModel):
    resume: str
    timeline: list[TimelineEvent]
    evidence: list[Evidence]

