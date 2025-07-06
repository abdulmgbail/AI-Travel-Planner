import requests

class CurrencyConverterTool:

    def __init__(self,api_key: str):
        self.api_key = api_key
        self.base_url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/"


    def convert_currency(self, from_currency: str, to_currency: str, amount: float) -> float:
        """
        Converts an amount from one currency to another using the ExchangeRate-API.

        Args:
            from_currency (str): The currency code to convert from.
            to_currency (str): The currency code to convert to.
            amount (float): The amount of money to convert.

        Returns:
            float: The converted amount in the target currency.
        """
        url = f"{self.base_url}/{from_currency}"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Error fetching exchange rates: {response.status_code} - {response.text}")
    
        conversion_rates = response.json()["conversion_rates"]
        if to_currency not in conversion_rates:
            raise ValueError(f"Currency '{to_currency}' not found in conversion rates.")
        
        converted_amount = amount * conversion_rates[to_currency]
        return converted_amount