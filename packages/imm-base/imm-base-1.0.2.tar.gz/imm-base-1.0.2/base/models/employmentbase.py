from pydantic import BaseModel, validator
from datetime import date, timedelta
from typing import Optional, List
from base.models.mixins import DurationMixin, DatePeriod
from base.models.utils import makeList, Duration


class EmploymentBase(DatePeriod, DurationMixin):
    job_title: str
    noc_code: str
    weekly_hours: float
    company: str
    city: str
    province: Optional[str]
    country: str

    @property
    def is_full_time(self):
        return self.weekly_hours >= 30

    # These are usually used for assessment
    
    # These are usually used  for word doc automation
    @property
    def part_time(self):
        return "Part time" if self.weekly_hours < 30 else ""

    @property
    def years(self):
        return Duration(self.start_date, self.end_date).years

    @property
    def months(self):
        return Duration(self.start_date, self.end_date).months

    def yearsOnDate(self, end_date):
        return Duration(self.start_date, self.end_date).yearsOnDate(end_date)

    def monthsOnDate(self, end_date):
        return Duration(self.start_date, self.end_date).monthsOnDate(end_date)

    @property
    def start_date_mmyyyy(self):
        return self.start_date.strftime("%b %Y")

    @property
    def end_date_mmyyyy(self):
        return self.end_date.strftime("%b %Y") if self.end_date else "Present"

    @property
    def is_present(self):
        return not self.end_date or self.end_date == "Present"
