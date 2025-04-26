import pytest
import pandas as pd
import openpyxl
from unittest.mock import patch, mock_open
from src.external_xls import get_external_xls

@pytest.fixture
def pd_Data_Frame():
    df = pd.DataFrame({'id': [650703.0], 'state': ['EXECUTED'], 'date': ['2023-09-05T11:30:32Z'],
                       'amount': [16210.0], 'currency_name': ['Sol'], 'currency_code': ['PEN'],
                       'from': ['Счет 58803664561298323391'], 'to': ['Счет 39745660563456619397'],
                       'description': ['Перевод организации']})
    return df

@patch("pandas.read_excel")
def test_get_external_xls(mock_xls, pd_Data_Frame):
    mock_xls.return_value = pd_Data_Frame
    assert get_external_xls("test_path") == [{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
                                              'amount': 16210.0, 'currency_name': 'Sol', 'currency_code': 'PEN',
                                              'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
                                              'description': 'Перевод организации'}]
    mock_xls.assert_called_once_with("test_path")


# @patch('builtins.open', new_callable=mock_open)
# @patch("pandas.read_excel")
# @patch("pandas.DataFrame")
# def test_get_external_xls(pd_Data_Frame, mock_xls, mock_file):
#    mock_xls.return_value = pd_Data_Frame
#    assert get_external_xls(pd_Data_Frame) == [{"id": "50", "state": "131"}, {"id": "21", "state": "2"}]
#    mock_file.assert_called_once_with("test")
#    mock_xls.assert_called_once()


def test_cod_error():
    with pytest.raises(FileNotFoundError, match="Файл не найден"):
        get_external_xls('transactions_excel.xlsx')