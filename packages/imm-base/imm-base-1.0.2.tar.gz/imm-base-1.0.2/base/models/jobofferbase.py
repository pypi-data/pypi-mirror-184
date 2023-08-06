from pydantic import BaseModel, validator
from typing import Optional
from datetime import date, timedelta
from pydantic.class_validators import root_validator
from base.utils.utils import speaking_list


class JobofferBase(BaseModel):
    job_title: str
    noc: str
    hours: float
    days: int
    wage_unit: str
    wage_rate: float
    ot_ratio: float
    permanent: bool
    work_start_date: Optional[date]
    job_duration: Optional[float]
    job_duration_unit: Optional[str]
    disability_insurance: bool
    dental_insurance: bool
    empolyer_provided_persion: bool
    extended_medical_insurance: bool
    extra_benefits: Optional[str]

    @property
    def has_benefits(self):
        return any(
            [
                self.disability_insurance,
                self.dental_insurance,
                self.empolyer_provided_persion,
                self.extended_medical_insurance,
                self.extra_benefits,
            ]
        )

    @property
    def benefits(self):
        benefits_list = []
        if self.disability_insurance:
            benefits_list.append("Disability insurance")
        if self.dental_insurance:
            benefits_list.append("Dental insurance")
        if self.empolyer_provided_persion:
            benefits_list.append("Empolyer provided persion")
        if self.extended_medical_insurance:
            benefits_list.append("Extended medical insurance")
        if self.extra_benefits:
            benefits_list.append(self.extra_benefits)
        return speaking_list(benefits_list)

    @root_validator
    def checkDuration(cls, values):
        if not values.get("permanent") and (
            not values.get("job_duration") or not values.get("job_duration_unit")
        ):
            raise ValueError(
                "Since it is not permanent job offer, so you have to specify the job duration and job duration unit in info-joboffer sheet"
            )
        return values

    @property
    def term(self):
        if self.permanent:
            return "Permanent"
        else:
            if not self.job_duration or not self.job_duration_unit:
                raise ValueError(
                    "Since you claimed the job offer is not permanent, you must spcify the job duration and duration unit"
                )
            return str(self.job_duration) + " " + self.job_duration_unit

    @property
    def full_part_time(self):
        return "full-time" if self.hours >= 30 else "part-time"

    @property
    def is_full_time(self):
        return True if self.hours >= 30 else False

    @property
    def salary(self):
        return "{:,.1f}".format(self.wage_rate)

    @property
    def weekly_hours(self):
        return "{:,.1f}".format(self.hours)

    @property
    def hourly_rate(self):
        rate = 0
        if self.wage_unit == "annually":
            rate = self.wage_rate / 52 / self.hours
        if self.wage_unit == "monthly":
            rate = self.wage_rate * 12 / 52 / self.hours
        if self.wage_unit == "weekly":
            rate = self.wage_rate / self.hours
        if self.wage_unit == "hourly":
            rate = self.wage_rate
        return "{0:.4g}".format(rate)

    @property
    def how_to_convert_to_hourly_rate(self):
        the_way = ""
        if self.wage_unit == "annually":
            rate = self.wage_rate / 52 / self.hours
            the_way = f"The annual wage is {'{0:.10g}'.format(self.wage_rate)}, and weekly working hours is {'{0:.4g}'.format(self.hours)}, so the hourly rate is {self.wage_rate}/52/{self.hours}={'{0:.4g}'.format(rate)}"
        if self.wage_unit == "monthly":
            rate = self.wage_rate * 12 / 52 / self.hours
            the_way = f"The monthly wage is {'{0:.10g}'.format(self.wage_rate)}, and weekly working hours is {'{0:.4g}'.format(self.hours)}, so the hourly rate is {self.wage_rate}*12/52/{self.hours}={'{0:.4g}'.format(rate)}"
        if self.wage_unit == "weekly":
            rate = self.wage_rate / self.hours
            the_way = f"The weekly wage is {'{0:.10g}'.format(self.wage_rate)}, and weekly working hours is {'{0:.4g}'.format(self.hours)}, so the hourly rate is {self.wage_rate}/{self.hours}={'{0:.4g}'.format(rate)}"
        if self.wage_unit == "hourly":
            rate = self.wage_rate
        return the_way

    @property
    def is_hourly_rate_converted(self):
        return False if self.wage_unit == "hourly" else True

    @property
    def hourly_rate_say(self):
        return f"${self.hourly_rate} per hour"

    @property
    def overtime_rate(self):
        return "{0:.4g}".format(float(self.hourly_rate) * self.ot_ratio)

    @property
    def overtime_rate_say(self):
        return "${rate:,.0f} per hour".format(rate=float(self.overtime_rate))

    @property
    def weekly_rate(self):
        rate = 0
        if self.wage_unit == "annually":
            rate = self.wage_rate / 52
        if self.wage_unit == "monthly":
            rate = self.wage_rate * 12 / 52
        if self.wage_unit == "weekly":
            rate = self.wage_rate
        if self.wage_unit == "hourly":
            rate = self.wage_rate * self.hours
        return "{0:.0f}".format(rate)

    @property
    def weekly_rate_say(self):
        return "${rate:,.0f} per week".format(rate=float(self.weekly_rate))

    @property
    def monthly_rate(self):
        rate = 0
        if self.wage_unit == "annually":
            rate = self.wage_rate / 12
        if self.wage_unit == "monthly":
            rate = self.wage_rate
        if self.wage_unit == "weekly":
            rate = self.wage_rate * 52 / 12
        if self.wage_unit == "hourly":
            rate = self.wage_rate * self.hours * 52 / 12
        return "{0:.0f}".format(rate)

    @property
    def monthly_rate_say(self):
        return "${rate:,.0f} per month".format(rate=float(self.monthly_rate))

    @property
    def annual_rate(self):
        rate = 0
        if self.wage_unit == "annually":
            rate = self.wage_rate
        if self.wage_unit == "monthly":
            rate = self.wage_rate * 12
        if self.wage_unit == "weekly":
            rate = self.wage_rate * 52
        if self.wage_unit == "hourly":
            rate = self.wage_rate * self.hours * 52
        return "{0:.0f}".format(rate)

    @property
    def annual_rate_say(self):
        return "${rate:,.0f} per year".format(rate=float(self.annual_rate))

    @property
    def requirements(self):
        reqs = [
            self.specific_edu_requirement,
            self.skill_experience_requirement,
            *self.other_requirements,
        ]
        return [req for req in reqs if req]

    # work start date + days (base on job_duration and job_duration_unit)
    @property
    def work_end_date(self):
        days = 0

        if self.job_duration_unit == "day":
            return self.work_start_date + timedelta(days=int(self.job_duration))
        if self.job_duration_unit == "week":
            return self.work_start_date + timedelta(weeks=int(self.job_duration))
        if self.job_duration_unit == "month":
            return self.work_start_date + timedelta(days=int(self.job_duration * 30))
        if self.job_duration_unit == "year":
            return self.work_start_date + timedelta(days=int(self.job_duration * 365))

    @property
    def is_primary_agriculture_position(self):
        return self.noc in ["0821", "0822", "8252", "8255", "8431", "8432", "8611"]

    @property
    def lmia_advertisement_variation(self):
        """Employers who wish to hire foreign workers in the following categories are subject to a variation in the advertising requirements:
        https://www.canada.ca/en/employment-social-development/services/foreign-workers/variations.html"""
        return self.noc in []  # TODO:
