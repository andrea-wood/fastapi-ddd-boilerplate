from dataclasses import dataclass
from app.user.domain.value_object.user_id import UserId
from app.user.domain.value_object.username import Username
from app.user.domain.value_object.point_balance import PointBalance


@dataclass(frozen=True, slots=True)
class User:
    id: UserId
    username: Username
    balance: PointBalance

    @classmethod
    def create(cls, user_id: UserId, username: Username) -> "User":
        return cls(id=user_id, username=username, balance=PointBalance(0))

    def credit_points(self, amount: int) -> "User":
        return User(
            id=self.id,
            username=self.username,
            balance=self.balance.credit(amount)
        )

    def debit_points(self, amount: int) -> "User":
        return User(
            id=self.id,
            username=self.username,
            balance=self.balance.debit(amount)
        )