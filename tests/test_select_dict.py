import pytest
from src.select_dict import select_from_dict


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
            ]

@pytest.mark.parametrize("my_string, expected",
    [
        (
            "Перевод организации",
            [{"id": "650703", "description": "Перевод организации"}],
        )
    ],
)

def test_select_dict(prices, my_string, expected) -> None:
    assert select_from_dict(prices, my_string) == expected


def test_type_select_dict(prices) -> None:
    with pytest.raises(TypeError):
        select_from_dict(prices, my_string=1) # type: ignore


def test_invalid_select_ict(prices_nou) -> None:
    with pytest.raises(KeyError):
        select_from_dict(prices_nou, "Перевод организации")