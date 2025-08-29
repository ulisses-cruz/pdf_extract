from datetime import date
from pydantic import BaseModel


class TimelineEvent(BaseModel):
    event_id: int
    event_name: str
    event_description: str
    event_date: date
    event_page_init: int
    event_page_end: int
