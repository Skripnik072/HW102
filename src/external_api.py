import requests
import os
from dotenv import load_dotenv


def get_user_convert(amount: str, currency: str) -> str:
    '''Функция запрашивает курс для конвертации заданной валюты'''

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    load_dotenv()
    headers = {
        'apikey': os.getenv('API_KEY')
    }
    response = requests.get(url, headers=headers, timeout=5)
    status_code = response.status_code
    print(response.status_code)
    if status_code == 200:
        result = response.json()
        return result["result"]
    else:
        return 'Ошибка при обращении к API 400 - error'


# cur_result = get_user_convert("100", "USD")
# print(cur_result)
