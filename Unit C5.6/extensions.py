import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CoinConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException('Не удалось произвести конвертацию. Валюты одинаковые')

        try:
            quote_tiker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать наименование валюты {quote}')

        try:
            base_tiker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать наименование валюты {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        url = f"https://api.apilayer.com/currency_data/convert?to={base_tiker}&from={quote_tiker}&amount={amount}"
        headers = {
            "apikey": "Ddo7bbHpEwfMTKUFXO9aSsmBfKq7S06d"
        }
        response = requests.request("GET", url, headers=headers)
        total_base = json.loads(response.content)

        return total_base