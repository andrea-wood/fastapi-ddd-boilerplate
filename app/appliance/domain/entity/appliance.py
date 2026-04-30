from dataclasses import dataclass

from app.appliance.domain.value_object.applicance_id import ApplicanceId
from app.appliance.domain.entity.part import Part

@dataclass(frozen=True, slots=True)
class Appliance:
    id: ApplicanceId
    name: str
    brand: str
    parts: list