import pytest
from app.user.domain.entity.user import User
from app.user.domain.value_object.user_id import UserId
from app.user.domain.value_object.username import Username


class TestUser:

    def test_creates_user(self):
        user = User.create(UserId.generate(), Username("band123"))
        assert user.username.value == "band123"
