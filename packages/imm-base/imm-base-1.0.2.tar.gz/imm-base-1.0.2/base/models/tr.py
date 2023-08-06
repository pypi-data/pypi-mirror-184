from datetime import date
from pydantic import BaseModel, root_validator, validator
from typing import Optional, List
from base.models.address import Address
from base.utils.canada import province_abbr

# 1. start date must be greater than today
# 2. end date must be greater than start date
class DurationModel(BaseModel):
    start_date: date
    end_date: date

    @validator("end_date")
    def endDateBigger(cls, end_date, values):
        start_date = values.get("start_date")
        the_date = end_date or date.today()
        if (the_date - start_date).days <= 0:
            raise ValueError(
                f"End date {the_date} is earlier than from date {start_date} for the given period"
            )
        return end_date

    @validator("start_date")
    def checkStartDate(cls, v):
        if (v - date.today()).days <= 0:
            raise ValueError("The start date must be greater than today")
        return v


class TrCase(BaseModel):
    service_in: str
    same_as_cor: bool
    applying_country: Optional[str]
    applying_status: Optional[str]
    applying_start_date: Optional[date]
    applying_end_date: Optional[date]
    consent_of_info_release: bool
    submission_date: Optional[date]

    @root_validator
    def checkCompletion(cls, values):
        same_as_cor = values.get("same_as_cor")
        applying_country = values.get("applying_country")
        applying_status = values.get("applying_status")
        applying_start_date = values.get("applying_start_date")
        applying_end_date = values.get("applying_end_date")
        if not same_as_cor and not all(
            [applying_country, applying_status, applying_start_date, applying_end_date]
        ):
            raise ValueError(
                "Since you are applying from a country different from your current residential country, so you have to fill all below rows:\napplying country, status, the start and end date of this status."
            )
        return values


class TrCaseIn(BaseModel):
    service_in: str
    application_purpose: Optional[str]  # TODO: consider
    original_entry_date: date
    original_entry_place: str
    original_purpose: str
    original_other_reason: Optional[str]
    most_recent_entry_date: Optional[date]
    most_recent_entry_place: Optional[str]
    doc_number: Optional[str]
    consent_of_info_release: bool
    submission_date: Optional[date]

    @root_validator
    def checkMostRecent(cls, values):
        most_recent_entry_date = values.get("most_recent_entry_date")
        most_recent_entry_place = values.get("most_recent_entry_place")
        original_entry_date = values.get("original_entry_date")
        if (
            most_recent_entry_date
            and original_entry_date
            and (most_recent_entry_date - original_entry_date).days <= 0
        ):
            raise ValueError(
                f"The most recent visiting date must later than the original one, but your input {most_recent_entry_date} is equal/earlier to the original {original_entry_date}"
            )

        if most_recent_entry_date and not most_recent_entry_place:
            raise ValueError(
                "You inputed most recent entry date, but most recent entry place is missed."
            )
        return values


class Visa(DurationModel):
    application_purpose: str
    visit_purpose: str
    funds_available: int
    name1: Optional[str]
    relationship1: Optional[str]
    address1: Optional[str]
    name2: Optional[str]
    relationship2: Optional[str]
    address2: Optional[str]


class Sp(DurationModel):
    school_name: str
    study_level: str
    study_field: str
    province: str
    city: str
    address: str
    dli: Optional[str]
    student_id: Optional[str]
    tuition_cost: Optional[str]
    room_cost: Optional[str]
    other_cost: Optional[str]
    fund_available: str
    paid_person: str
    other: Optional[str]
    dual_intent:bool
    family_tie:Optional[str]
    economic_tie:Optional[str]
    other_tie:Optional[str]
    refused_case:bool
    refusal_explain:Optional[str]

class Wp(DurationModel):
    work_permit_type: str
    application_title: Optional[str]
    dual_intent: bool
    family_tie: Optional[str]
    economic_tie: Optional[str]
    other_tie: Optional[str]
    other_explain: Optional[str]
    employer_name: Optional[str]
    employer_address: Optional[str]
    work_province: Optional[str]
    work_city: Optional[str]
    work_address: Optional[str]
    job_title: Optional[str]
    brief_duties: Optional[str]
    lmia_num_or_offer_num: Optional[str]
    # pnp_certificated: bool
    caq_number: Optional[str]
    expiry_date: Optional[date]
    refused_case: bool
    refusal_explain: Optional[str]

    @root_validator
    def check_refused_case(cls, values):
        if values.get("refused_case") and not values.get("refusal_explain"):
            raise ValueError("It is refused case, but no explaination for the refusal")
        return values

    @validator("brief_duties")
    def longer_than_5(cls, v):
        if v and len(v) < 5:
            raise ValueError("must longer than 5 characters")
        return v

    @root_validator
    def checkLMIA_OfferNum(cls, values):
        work_permit_type = values.get("work_permit_type")
        lmia_num_or_offer_num = values.get("lmia_num_or_offer_num")
        if (
            work_permit_type == "Labour Market Impact Assessment Stream"
            and not lmia_num_or_offer_num
        ):
            raise ValueError(
                "Since the work permit type is LMIA stream, LMIA number is required"
            )
        if (
            work_permit_type
            in [
                "Exemption from Labour Market Impact Assessment",
                "Live-in Caregiver Program",
                "Start-up Business Class",
            ]
            and not lmia_num_or_offer_num
        ):
            raise ValueError(
                "Since you are applying employer specific work permit, so the number of Employer portal offer of employment is required"
            )

        return values

    @root_validator
    def check_others(cls, values):
        application_title = values.get("application_title", None)
        work_permit_type = values.get("work_permit_type")
        if not application_title:
            values["application_title"] = f"Application for {work_permit_type}"

        brief_duties = values.get("brief_duties")
        work_permit_type = values.get("work_permit_type")

        open_work_permits = [
            "Open Work Permit",
            "Post Graduation Work Permit",
            "Co-op Work Permit",
            "Open Work Permit for Vulnerable Workers",
        ]
        # if open work permit and has no brief duties
        if not brief_duties:
            if work_permit_type in open_work_permits:
                values["brief_duties"] = "Not applicable"
            else:
                raise ValueError(
                    f"Since your work permit type is {work_permit_type}, you should have employer already, but you didn't input brief duties"
                )

        # if non open work permit but no company info etc...
        if work_permit_type not in open_work_permits:
            employer_name = values.get("employer_name")
            employer_address = values.get("employer_address")
            work_province = values.get("work_province")
            work_city = values.get("work_city")
            work_address = values.get("work_address")
            if not all(
                [
                    employer_name,
                    employer_address,
                    work_province,
                    work_city,
                    work_address,
                ]
            ):
                raise ValueError(
                    "Since your application is not for open work permit, so you should have employer, but no all of employer's information was provided."
                )

        # check province
        work_province = values.get("work_province")
        if work_province and work_province not in province_abbr:
            raise ValueError(
                f"{work_province} is not a valid Canada province abbrevation"
            )

        return values


class VrInCanada(DurationModel):
    application_purpose: str
    visit_purpose: str
    other_explain: Optional[str]
    funds_available: int
    paid_person: str
    other: Optional[str]
    name1: str
    relationship1: str
    address1: str
    name2: Optional[str]
    relationship2: Optional[str]
    address2: Optional[str]
    reason_for_vr: Optional[str]


class SpInCanada(DurationModel):
    application_purpose: str
    apply_work_permit: bool
    work_permit_type: Optional[str]
    caq_number: Optional[str]
    expiry_date: Optional[date]
    school_name: str
    study_level: str
    study_field: str
    province: str
    city: str
    address: str
    dli: Optional[str]
    student_id: str
    tuition_cost: Optional[str]
    room_cost: Optional[str]
    other_cost: Optional[str]
    fund_available: str
    paid_person: str
    other: Optional[str]


class WpInCanada(DurationModel):
    application_purpose: str
    caq_number: Optional[str]
    expiry_date: Optional[date]
    work_permit_type: str
    employer_name: Optional[str]
    employer_address: Optional[str]
    work_province: Optional[str]
    work_city: Optional[str]
    work_address: Optional[str]
    job_title: Optional[str]
    brief_duties: Optional[str]
    lmia_num_or_offer_num: Optional[str]
    pnp_certificated: bool

    @validator("brief_duties")
    def longer_than_5(cls, v):
        if len(v) < 5:
            raise ValueError("must longer than 5 characters")
        return v

    @root_validator
    def lmia_number_check(cls, values):
        wp_type = values.get("work_permit_type")
        number = values.get("lmia_num_or_offer_num")
        if wp_type == "Labour Market Impact Assessment Stream" and (
            int(number) < 6000000 or int(number) > 99999999
        ):
            raise ValueError("LMIA number must between 6,000,000  and 99,999,999")

        return values

    @root_validator
    def checkLMIA_OfferNum(cls, values):
        work_permit_type = values.get("work_permit_type")
        lmia_num_or_offer_num = values.get("lmia_num_or_offer_num")
        if (
            work_permit_type == "Labour Market Impact Assessment Stream"
            and not lmia_num_or_offer_num
        ):
            raise ValueError(
                "Since the work permit type is LMIA stream, LMIA number is required"
            )
        if (
            work_permit_type
            in [
                "Exemption from Labour Market Impact Assessment",
                "Live-in Caregiver Program",
                "Start-up Business Class",
            ]
            and not lmia_num_or_offer_num
        ):
            raise ValueError(
                "Since you are applying employer specific work permit, so the number of Employer portal offer of employment is required"
            )

        return values


class TrBackground(BaseModel):
    q1a: bool
    q1b: bool
    q1c: Optional[str]
    q2a: bool
    q2b: bool
    q2c: bool
    q2d: Optional[str]
    q3a: bool
    q3b: Optional[str]
    q4a: bool
    q4b: Optional[str]
    q5: bool
    q6: bool
