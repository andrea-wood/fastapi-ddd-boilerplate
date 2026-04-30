import uuid

class AggregateRootId:
    def __init__(self, uuid: str):
        self._uuid = uuid

    @property
    def value(self) -> str:
        return self._uuid

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self._uuid == other._uuid

    def __hash__(self) -> int:
        return hash(self._uuid)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._uuid!r})"