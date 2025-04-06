import pytest

from src.taxes import calculate_taxes


@pytest.fixture
def prices() -> list:
    return [100, 200, 300]


@pytest.mark.parametrize("tax_rate, expected", [(10, [110, 220, 330]),
                                                (15, [115, 230, 345]),
                                                (20, [120, 240, 360])])
def test_calculate_taxes(prices: list, tax_rate: int, expected: list) -> None:
    assert calculate_taxes(prices, tax_rate) == expected


def test_invalid_tax_rate(prices: list) -> None:
    with pytest.raises(ValueError):
        calculate_taxes(prices, tax_rate=-1)


def test_invalid_prices(prices: list) -> None:
    with pytest.raises(ValueError):
        calculate_taxes([0, -10], tax_rate=10)
