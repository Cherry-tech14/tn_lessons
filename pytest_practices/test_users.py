import pytest

@pytest.fixture
def users():
    return ["Alex", "Jordan", "Taylor"]
def test_number_of_users(users):
    assert len(users) == 3