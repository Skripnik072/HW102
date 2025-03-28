import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account

assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"

@pytest.fixture
def fixture_card():
    return (7000792289606361)


def test_invalid_number_card(fixture_card):
    with pytest.raises(ValueError):
        get_mask_card_number(7000)


def test_empty_number_card(fixture_card):
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_empty_number_card(fixture_card):
    with pytest.raises(ValueError):
        get_mask_card_number("7000роgj35648749")


assert get_mask_account(73654108430135874305) == "**4305"


@pytest.fixture
def fixture_account():
    return (73654108430135874305)


def test_invalid_number_card(fixture_account):
    with pytest.raises(ValueError):
        get_mask_account(7000)


def test_empty_number_card(fixture_account):
    with pytest.raises(ValueError):
        get_mask_account("")


def test_empty_number_card(fixture_account):
    with pytest.raises(ValueError):
        get_mask_account("7000роgj3564dfgh8749")