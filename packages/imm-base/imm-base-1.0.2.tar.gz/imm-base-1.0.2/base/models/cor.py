from datetime import date
from pydantic import BaseModel, EmailStr, root_validator
from typing import List, Optional
from base.models.mixins import DatePeriod
from base.models.utils import checkRow


class COR(DatePeriod):
    start_date: date
    end_date: Optional[date]
    country: str
    status: str

    @root_validator
    def checkCompletion(cls, values):
        all_fields = [
            "country",
            "status",
            "start_date",
            "end_date",
        ]
        required_fields = [
            "country",
            "status",
            "start_date",
        ]
        checkRow(values, all_fields, required_fields)

        return values


class CORs(object):
    # Frist row must be current residence
    def __init__(self, cors: List[COR]):
        self.cors = cors

    @property
    def current(self):
        ccor = [country for country in self.cors if country.end_date == None]
        if len(ccor) == 1:
            return ccor[0]
        elif len(ccor) == 0 and len(self.cors) > 0:
            return self.cors[0]
        else:
            raise ValueError("No residence data, please check")

    @property
    def previous(self):
        if len(self.cors) == 0:
            raise Exception("There is no residence data, please check")
            return
        if len(self.cors) == 1:
            # There is only one row data, which is considered current residence. So, there is no previous residence.
            return None
        return self.cors[1:]
