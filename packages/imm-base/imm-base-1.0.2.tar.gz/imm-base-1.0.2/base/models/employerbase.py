from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from base.models.utils import normalize


class EmployerBase(BaseModel):
    legal_name: str
    operating_name: Optional[str]
    website: Optional[str]

    _normalize_legal_name = validator(
        "legal_name", allow_reuse=True, check_fields=False
    )(normalize)
    _normalize_operating_name = validator(
        "operating_name", allow_reuse=True, check_fields=False
    )(normalize)

    @property
    def preferred_name(self):
        return self.operating_name if self.operating_name else self.legal_name
