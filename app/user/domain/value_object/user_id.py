import uuid

from app.shared.domain.value_object.aggregate_root_id import AggregateRootId

class UserId(AggregateRootId):

    def __init__(self, value: str):
        try:
            uuid.UUID(value)  # valida formato
        except ValueError:
            raise ValueError(f"Invalid UserId: {value}")
        super().__init__(value)  # passa a AggregateRootId._uuid

    @classmethod
    def generate(cls) -> "UserId":
        return cls(str(uuid.uuid4()))