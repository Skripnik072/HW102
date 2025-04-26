import pytest
import os
from unittest.mock import patch, mock_open
from src.external_csv import get_external_csv


@patch('builtins.open', new_callable=mock_open)
@patch("csv.DictReader")
def test_get_external_csv(mock_csv, mock_file):
    mock_csv.return_value = [{"id": "test", "state": "state", "date": "date",
                             "amount": "amount", "currency_name": "currency_name",
                             "currency_code": "currency_code", "from": "from", "to": "to",
                             "description": "description"}]
    assert get_external_csv("test") == [{"id": "test", "state": "state", "date": "date",
                             "amount": "amount", "currency_name": "currency_name",
                             "currency_code": "currency_code", "from": "from", "to": "to",
                             "description": "description"}]
    mock_file.assert_called_once_with("test", encoding='utf-8')
    mock_csv.assert_called_once()


def test_cod_error():
    with pytest.raises(FileNotFoundError, match="Файл не найден"):
        get_external_csv('transactions.csv')