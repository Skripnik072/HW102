import pytest
from src.transf_list import list_from_dict


@pytest.fixture
def prices_nou():
    return [
                {"id": "650703", "scription": "Перевод физическому лицу"},
                {"id": "3598919", "scription": "Перевод с карты на карту"},
            ]

@pytest.fixture
def prices():
    return [
                {"id": "650703", "description": "Перевод организации"},
                {"id": "3598919", "description": "Перевод с карты на карту"},
                {'id': '593027',  "description": "Открытие вклада"},
                {"id": "650705", "description": "Перевод организации"},
            ]

@pytest.mark.parametrize("my_dict, expected",
    [
        (
            {'Перевод организации': 0, 'Перевод с карты на карту': 0, 'Открытие вклада': 0},
            {'Перевод с карты на карту': 1, 'Перевод организации': 2, 'Открытие вклада': 1},
        )
    ],
)

def test_transf_list(prices, my_dict, expected) -> None:
    assert list_from_dict(prices, my_dict) == expected


def test_type_transf_list(prices) -> None:
    with pytest.raises(TypeError):
        list_from_dict(prices, my_dict=[]) # type: ignore


def test_invalid_transf_dict(prices_nou) -> None:
    with pytest.raises(KeyError):
        list_from_dict(prices_nou, {"Перевод организации": 0})