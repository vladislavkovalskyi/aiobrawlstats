from datetime import datetime
from typing import Optional, List, Iterable

from pydantic import BaseModel, Field, validator


class ScheduledEventLocation(BaseModel):
    id: int = None
    mode: str = None
    map: str = None
    modificator: Optional[List[str]] = None


class ScheduledEvent(BaseModel):
    start_time: datetime = Field(alias="startTime")
    end_time: datetime = Field(alias="endTime")
    event: ScheduledEventLocation = None

    @validator("end_time", "start_time", pre=True)
    def check_names_not_empty(cls, v) -> datetime:
        return datetime(
            int(v[0:4]), int(v[4:6]), int(v[6:8]), int(v[9:11]), int(v[11:13]), int(v[13:15])
        )


class ScheduledEvents(BaseModel):
    __root__: List[ScheduledEvent] = None

    def __iter__(self) -> Iterable:
        return iter(self.__root__)

    def __getitem__(self, item):
        return self.__root__[item]
