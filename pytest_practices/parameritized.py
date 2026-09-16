import pytest
from calculator import add


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (10, 5, 15),
        (7, 8, 15),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected