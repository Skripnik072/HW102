import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def fixture_list_dict() -> list:
    return [{"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"}]


@pytest.fixture
def fixture_expected() -> str:
    return ("EXECUTED")


@pytest.fixture
def fixture_canceled() -> str:
    return ("CANCELED")


@pytest.mark.parametrize(
    "my_list, state, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            "CANCELED",
            [{"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"}],
        ),
    ],
)
def test_filter_by_state(my_list: list, state: str, expected: list) -> None:
    assert filter_by_state(my_list, state) == expected


def test_type_list_dict() -> None:
    with pytest.raises(TypeError):
        filter_by_state([9970909])


def test_empty_list_dict() -> None:
    with pytest.raises(ValueError):
        filter_by_state([], "EXECUTED")


def test_invalid_key(fixture_list_dict: list) -> None:
    with pytest.raises(KeyError):
        filter_by_state(fixture_list_dict, "reserved")


@pytest.mark.parametrize(
    "my_list, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "CANCELED", "date": "2019-07-04T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            [
                {"id": 41428829, "state": "CANCELED", "date": "2019-07-04T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2020-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2020-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_sort_by_date(my_list: list, expected: str) -> None:
    assert sort_by_date(my_list) == expected


@pytest.mark.parametrize(
    "my_list, reverse, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "CANCELED", "date": "2019-07-04T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "CANCELED", "date": "2019-07-04T18:35:29.512364"},
            ],
        )
    ],
)
def test_sort_by_date_reverse(my_list: list, reverse: bool, expected: list) -> None:
    assert sort_by_date(my_list, reverse) == expected


def test_type_list() -> None:
    with pytest.raises(TypeError):
        sort_by_date("01011966", reverse=False)


def test_empty_list_() -> None:
    with pytest.raises(ValueError):
        sort_by_date([])


def test_invalid_date() -> None:
    with pytest.raises(ValueError):
        sort_by_date([{"id": 939719570, "state": "EXECUTED", "date": "HJGF-HH-JJT02:08:58.425572"}])
