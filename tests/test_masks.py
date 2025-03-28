import pytest
from src.masks import get_mask_card_number

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
