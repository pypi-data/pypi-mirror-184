from datetime import date, timedelta
from typing import List
from base.models.employmentbase import EmploymentBase


class EmploymentHistory:
    def __init__(self, employment_list: List[EmploymentBase]):
        self.employment_list = employment_list
        for emp in employment_list:
            if not isinstance(emp, EmploymentBase):
                raise ValueError(
                    f"{employment_list} is not a list of EmploymentBase objects"
                )

    # These properties are usually used to do assessment
    
    # these properties are usually used to do word doc automation
    @property
    def initial_start_date(self):
        return min([emp.start_date for emp in self.employment_list])

    @property
    def final_end_date(self):
        end_dates = []
        for emp in self.employment_list:
            if emp.is_present:
                return "Present"
            end_dates.append(emp.end_date)
        return max(end_dates) or "Present"

    @property
    def position_number(self):
        return len(set([emp.job_title for emp in self.employment_list]))

    @property
    def position_number_say(self):
        number = len(set([emp.job_title for emp in self.employment_list]))
        return str(number) + " position" if number <= 1 else str(number) + " positions"

    def qualified_employment(self, program):
        return [job for job in self.employment_list if getattr(job, program)]
