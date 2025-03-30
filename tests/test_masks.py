import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def fixture_card()->int:
    return (7000792289606361)


def test_get_mask_card_number_error(fixture_card: str) -> None:
    with pytest.raises(TypeError):
        get_mask_card_number(fixture_card)


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_type_card_number() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("jkfdl")


def test_invalid_number_card() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("7000")


def test_empty_number_card() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_incorrect_number_car() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("7000роgj35648749")


@pytest.fixture
def fixture_account() -> int:
    return (73654108430135874305)


def test_get_mask_account() -> None:
    assert get_mask_account("73654108430135874305") == "**4305"


def test_type_account() -> None:
    with pytest.raises(ValueError):
        get_mask_account("jkfdl")


def test_invalid_number_account() -> None:
    with pytest.raises(ValueError):
        get_mask_account("7000")


def test_empty_number_account() -> None:
    with pytest.raises(ValueError):
        get_mask_account("")


def test_incorrect_number_card() -> None:
    with pytest.raises(ValueError):
        get_mask_account("7000роgj3564dfgh8749")
