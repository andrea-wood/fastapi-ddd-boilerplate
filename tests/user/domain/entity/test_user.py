import pytest
from app.user.domain.entity.user import User
from app.user.domain.value_object.user_id import UserId
from app.user.domain.value_object.username import Username
from app.user.domain.value_object.point_balance import PointBalance
from dataclasses import FrozenInstanceError


class TestUser:

    def _make_user(self, username: str = "band123") -> User:
        return User.create(UserId.generate(), Username(username))

    # --- creazione ---

    def test_creates_user(self):
        user = self._make_user()
        assert user.username.value == "band123"
