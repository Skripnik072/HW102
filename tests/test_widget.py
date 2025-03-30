import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def fixture_card() -> str:
    return "Maestro 7000792289606361"


@pytest.fixture
def fixture_account() -> str:
    return "Счет 73654108430135874305"


@pytest.mark.parametrize(
    "my_string, expected",
    [
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(my_string: str, expected: str) -> None:
    assert mask_account_card(my_string) == expected


def test_type_number_card_or_account() -> None:
    with pytest.raises(TypeError):
        mask_account_card([10, 12, 20]) # type: ignore


def test_invalid_number_card_or_account() -> None:
    with pytest.raises(ValueError):
        mask_account_card("7000")


def test_empty_number_card_or_account(fixture_card: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card("")


@pytest.fixture
def fixture_date() -> str:
    return "2024-03-11T02:26:18.671407"


def test_get_date(fixture_date: str) -> None:
    assert get_date(fixture_date) == "11.03.2024"


def test_type_date() -> None:
    with pytest.raises(TypeError):
        get_date(101220) # type: ignore


def test_empty_date() -> None:
    with pytest.raises(ValueError):
        get_date("")


def test_invalid_date() -> None:
    with pytest.raises(ValueError):
        get_date("ghfdslkhslkh")
