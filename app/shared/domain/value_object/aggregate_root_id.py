import uuid
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class AggregateRootId:
    value: str

    def __post_init__(self):
        if not self.value:
            raise ValueError("Id cannot be empty")