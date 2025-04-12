import pytest

from src.decorators import log, my_function


def test_my_decorators():
    @log()
    def my_function(x, y):
        return x + y

    result = my_function(3, 5)
    assert result == 8


def test_my_decorators_in_file():
    @log(filename='mylog.txt')
    def my_function(x, y):
        return x + y

    result = my_function(3, 4)
    assert result == 7


def test_log_error():
    with pytest.raises(Exception, match="Ошибка в работе декоратора"):
        my_function()


def test_log_output(capsys):
    my_function(3, 1)
    captured = capsys.readouterr()
    assert captured.out == 'my_function ok Time for work: -4.76837158203125e-07\n\n'
