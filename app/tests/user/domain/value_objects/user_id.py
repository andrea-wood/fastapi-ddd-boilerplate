import pytest
from src.user.domain.value_objects.user_id import UserId

class TestUserId:

    def test_creates_with_valid_uuid(self):
        user_id = UserId("550e8400-e29b-41d4-a716-446655440000")
        assert user_id.value == "550e8400-e29b-41d4-a716-446655440000"

    def test_generates_unique_ids(self):
        id1 = UserId.generate()
        id2 = UserId.generate()
        assert id1 != id2

    def test_equality_same_uuid(self):
        id1 = UserId("550e8400-e29b-41d4-a716-446655440000")
        id2 = UserId("550e8400-e29b-41d4-a716-446655440000")
        assert id1 == id2

    def test_inequality_different_uuid(self):
        id1 = UserId.generate()
        id2 = UserId.generate()
        assert id1 != id2

    def test_raises_on_invalid_uuid(self):
        with pytest.raises(ValueError):
            UserId("not-a-valid-uuid")