import pytest
from typing import Any, Generator
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.parametrize(
    "transactions, currency, expected",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
        )
    ],
)
def test_filter_by_currency(transactions: list, currency: str, expected: list) -> None:
    result = filter_by_currency(transactions, currency)
    assert next(result) == expected


def test_type_list_dic() -> None:
    with pytest.raises(TypeError):
        filter_by_currency("test")  # type: ignore


def test_empty_list_diс() -> None:
    with pytest.raises(ValueError):
        next(filter_by_currency([], ""))


@pytest.mark.parametrize(
    "transactions, expected",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            "Перевод организации",
        )
    ],
)
def test_transaction_descriptions(transactions: list, expected: str) -> None:
    result = transaction_descriptions(transactions)
    assert next(result) == expected


def test_type_list_dct() -> None:
    with pytest.raises(TypeError):
        transaction_descriptions("test")  # type: ignore


def test_empty_list_dct() -> None:
    with pytest.raises(ValueError):
        next(transaction_descriptions([]))


@pytest.mark.parametrize(
    "begin_number, end_number, expected",
    [(1, 2, ["0000 0000 0000 0001"]), (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002"])],
)
def test_card_number_generator(begin_number: int, end_number: int, expected: str) -> None:
    assert card_number_generator(begin_number, end_number) == expected


def test_type_number() -> None:
    with pytest.raises(TypeError):
        card_number_generator("test")  # type: ignore


def test_uncorrect_number() -> None:
    with pytest.raises(ValueError):
        next(card_number_generator(1, -3))


def test_uncorrect_numb() -> None:
    with pytest.raises(TypeError):
        next(card_number_generator(-3))
