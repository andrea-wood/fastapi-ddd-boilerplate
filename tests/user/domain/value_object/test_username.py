import pytest
from app.user.domain.value_object.username import Username

class TestUsername:

    def test_creates_valid_username(self):
        username = Username("band123")
        assert username.value == "band123"

    def test_raises_on_empty(self):
        with pytest.raises(ValueError):
            Username("")

    def test_raises_too_short(self):
        with pytest.raises(ValueError):
            Username("ab")

    def test_raises_too_long(self):
        with pytest.raises(ValueError):
            Username("a" * 51)

    def test_raises_non_alphanumeric(self):
        with pytest.raises(ValueError):
            Username("band_123")

    def test_equality(self):
        assert Username("band123") == Username("band123")

    def test_inequality(self):
        assert Username("band123") != Username("other123")

    def test_immutable(self):
        username = Username("band123")
        with pytest.raises(Exception):
            username.value = "other"  # frozen=True impedisce modifica