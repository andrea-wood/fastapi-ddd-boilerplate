from dataclasses import dataclass
from app.user.domain.value_object.user_id import UserId
from app.user.domain.value_object.username import Username


@dataclass(frozen=True, slots=True)
class User:
    id: UserId
    username: Username

    @classmethod
    def create(cls, user_id: UserId, username: Username) -> "User":
        return cls(id=user_id, username=username)