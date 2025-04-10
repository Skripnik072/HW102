import pytest
from src.decorators import log, my_function
from src.decorators import my_decorators


def test_my_decorator():
    @my_decorators
    def my_function(x, y):
        return x + y

    result = my_function(3, 5)
    assert result == 8


def test_log():
    with pytest.raises(Exception, match="Max retries exceeded"):
        my_function()