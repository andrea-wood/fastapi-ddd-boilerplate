import re

from dataclasses import dataclass

from pydantic import constr

USERNAME_REGEX = re.compile(r"^[a-zA-Z0-9]+$")

@dataclass(frozen=True,slots=True)
class Username:
    value: str

    def __post_init__(self):
        if not self.value:
            raise ValueError("Username cannot be empty")
        if len(self.value) < 3:
            raise ValueError("Username must be at least 3 characters")
        if len(self.value) > 50:
            raise ValueError("Username cannot exceed 50 characters")
        if not USERNAME_REGEX.match(self.value):
            raise ValueError("Username must contain only letters and numbers")