import requests
import config
def get_rates(api_key):
    response = requests.get(f'{config.API_URL}? app_id={config.api_key}')
    if response.status_code != 200:
        raise Exception('Failed to retrieve rates')
    data = response.json()
    return data['rates']

def convert_currencies(rates,base_currency,target_currency,amount):
    if base_currency == target_currency:
        return amount
    else:
        rate = rates[target_currency]/rates[base_currency]
        return amount * rate

class CurrencyConverter:
    def __int__(self, api_key):
        self.rates = get_rates(api_key)

    def convert(self, base_currency, target_currency, amount):
        rates = self.rates
        if base_currency != 'RUB':
            amount = convert_currencies(rates, base_currency, 'RUB', amount)
        if target_currency != 'RUB':
            amount = convert_currencies(rates, 'RUB', target_currency, amount)
        return amount
