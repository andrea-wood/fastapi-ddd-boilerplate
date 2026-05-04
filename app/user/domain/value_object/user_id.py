import uuid

from dataclasses import dataclass
from app.shared.domain.value_object.aggregate_root_id import AggregateRootId

@dataclass(frozen=True, slots=True)
class UserId(AggregateRootId):
    def __post_init__(self):
        try:
            uuid.UUID(self.value)
        except ValueError:
            raise ValueError(f"Invalid UserId: {self.value}")

    @classmethod
    def generate(cls) -> "UserId":
        return cls(str(uuid.uuid4()))