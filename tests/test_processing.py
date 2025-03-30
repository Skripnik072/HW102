import pytest
from src.processing import filter_by_state
from src.processing import sort_by_date


@pytest.fixture
def fixture_list_dict():
    return [{'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}]


@pytest.mark.parametrize("my_list, state, expected", [
                         ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                         {'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}],
                          'EXECUTED',
                          [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),

                          ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}],
                          'CANCELED',
                          [{'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}]),])


def test_filter_by_state(my_list, state, expected):
    assert filter_by_state(my_list, state) == expected


def test_type_list_dict(fixture_list_dict):
    with pytest.raises(TypeError):
        filter_by_state(9970909)


def test_empty_list_dict():
    with pytest.raises(ValueError):
        filter_by_state([], 'EXECUTED')


def test_invalid_key(fixture_list_dict):
    with pytest.raises(KeyError):
        filter_by_state(fixture_list_dict,'reserved')


@pytest.mark.parametrize("my_list, expected", [
                         ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                         {'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-04T18:35:29.512364'},
                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}],
                          [{'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-04T18:35:29.512364'},
                          {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),

                          ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2020-07-03T18:35:29.512364'},
                           {'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}],
                           [{'id': 41428829, 'state': 'EXECUTED', 'date': '2020-07-03T18:35:29.512364'},
                           {'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),])


def test_sort_by_date(my_list, expected):
    assert sort_by_date(my_list) == expected