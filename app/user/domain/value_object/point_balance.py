from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class PointBalance:
    value: int

    def __post_init__(self):
        if self.value < 0:
            raise ValueError("Balance cannot be negative")

    def credit(self, amount: int) -> "PointBalance":
        return PointBalance(self.value + amount)

    def debit(self, amount: int) -> "PointBalance":
        if amount > self.value:
            raise ValueError("Insufficient balance")
        return PointBalance(self.value - amount)