# write a pytest test file
import pytest
from example_stats import is_even

@pytest.mark.parametrize("n,expected", [
    (2, True),
    (3, False),
    (0, True),
    (-4, True),
])
def test_is_even(n, expected):
    assert is_even(n) == expected

def test_is_even_typeerror():
    with pytest.raises(TypeError):
        is_even("not a number")
