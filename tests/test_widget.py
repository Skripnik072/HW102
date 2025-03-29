import pytest
from src.widget import mask_account_card
# from widget import get_date


@pytest.fixture
def fixture_card():
    return ("Maestro 7000792289606361")


@pytest.fixture
def fixture_account():
    return ("Счет 73654108430135874305")


@pytest.mark.parametrize("my_string, expected",
                         [("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
                         ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
                         ("Счет 73654108430135874305", "Счет **4305")],)


def test_mask_account_card(my_string, expected):
    assert mask_account_card(my_string) == expected


def test_type_number_card_or_account():
    with pytest.raises(TypeError):
        mask_account_card([10, 12, 20])