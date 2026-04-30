from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Point:
    value: int

    def __post_init__(self):
        if self.value < 0:
            raise ValueError("Points cannot be negative")
    
    def add(self, other: "Point") -> "Point":
        return Point(self.value + other.value)
    
    def subtract(self, other: "Point") -> "Point":
        if other.value > self.value:
            raise ValueError("Insufficient points")
        return Point(self.value - other.value)