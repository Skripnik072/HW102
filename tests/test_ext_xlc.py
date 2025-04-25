import pytest
import pandas as pd
import openpyxl
from unittest.mock import patch, mock_open
from src.external_xls import get_external_xls


@patch('builtins.open', new_callable=mock_open)
@patch("pd.read_excel")
def test_get_external_xls(mock_xls, mock_file):
    mock_xls.return_value = [{"id": "test", "state": "state", "date": "date",
                             "amount": "amount", "currency_name": "currency_name",
                             "currency_code": "currency_code", "from": "from", "to": "to",
                             "description": "description"}]
    assert get_external_xls("test") == [{"id": "test", "state": "state", "date": "date",
                             "amount": "amount", "currency_name": "currency_name",
                             "currency_code": "currency_code", "from": "from", "to": "to",
                             "description": "description"}]
    mock_file.assert_called_once_with("test")
    mock_xls.assert_called_once()


def test_cod_error():
    with pytest.raises(FileNotFoundError, match="Файл не найден"):
        get_external_xls('transactions.csv')