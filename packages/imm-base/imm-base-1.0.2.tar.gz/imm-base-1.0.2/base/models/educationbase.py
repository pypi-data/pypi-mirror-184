from functools import reduce
from pydantic import BaseModel, validator
from datetime import date
from typing import Optional, List
from base.models.mixins import DurationMixin, DatePeriod
from base.models.utils import makeList, normalize

"""
with properties of start_from and end_to got from mixin
"""
education_level = {
    "None": 0,
    "Less than high school": 0,
    "High school": 1,
    "Certificate/Diploma(Trade)": 2,
    "Diploma/Certificate": 3,
    "Associate": 4,
    "Bachelor": 5,
    "Post-graduate diploma": 6,
    "Master": 7,
    "Doctor": 8,
}


class EducationBase(DatePeriod, DurationMixin):
    school_name: str
    education_level: str
    field_of_study: str

    _normalize_school_name = validator(
        "school_name", allow_reuse=True, check_fields=False
    )(normalize)
    _normalize_field_of_study = validator(
        "field_of_study", allow_reuse=True, check_fields=False
    )(normalize)

    @property
    def level_in_num(self):
        return education_level[self.education_level]


class EducationHistory:
    def __init__(self, edu_list: List[EducationBase]):
        self.edu_list = edu_list

    # total education years
    @property
    def years(self):
        return reduce(lambda a, b: a.lengthOfYears + b.lengthOfYears, self.edu_list)

    @property
    def highest(self):
        edu_indeies = [education_level[edu.education_level] for edu in self.edu_list]
        if len(edu_indeies) > 0:
            highest_num = max(edu_indeies)
        else:
            return None
        for k, v in education_level.items():
            if v == highest_num:
                return k

    @property
    def highestEducation(self):
        highest_edu = [
            edu
            for edu in self.edu_list
            if edu.education_level == self.highest and edu.end_date
        ]  # edu.end_date should not be empty, which means it's ongoing education.
        if len(highest_edu) > 0:
            return highest_edu[0]

    # return highest post-secondary education only
    @property
    def highestPostSecondaryEducation(self):
        highest_edu = [
            edu
            for edu in self.edu_list
            if edu.education_level == self.highest
            and edu.end_date
            and education_level[edu.education_level] >= 2
        ]
        if len(highest_edu) > 0:
            return highest_edu[0]

    @property
    def high_school(self):
        return [edu for edu in self.edu_list if edu.education_level == "High school"]

    @property
    def post_secondary(self):
        return [
            edu
            for edu in self.edu_list
            if edu.education_level not in ["High school", "None"]
        ]

    def post_secondary_in_ca_prov(self, province):
        return [
            edu
            for edu in self.edu_list
            if edu.education_level not in ["High school", "None"]
            and edu.province == province
        ]

    def post_secondary_in_ca_but_not_in_prov(self, province):
        return [
            edu
            for edu in self.edu_list
            if edu.education_level not in ["High school", "None"]
            and edu.province != province
            and edu.country == "Canada"
        ]

    @property
    def post_secondary_not_in_ca(self):
        return [
            edu
            for edu in self.edu_list
            if edu.education_level not in ["High school", "None"]
            and edu.country != "Canada"
        ]
