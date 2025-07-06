import os
from dotenv import load_dotenv
load_dotenv()
from langchain.tools import tool
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper

@tool
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers together.
    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of a and b.
    """
    return a + b

@tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiplies two numbers together.
    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The product of a and b.
    """
    return a * b


@tool
def currency_conversion(amount: float, from_currency: str, to_currency: str) -> float:
    """Converts an amount from one currency to another using Alpha Vantage API.
    
    Args:
        amount (float): The amount of money to convert.
        from_currency (str): The currency code to convert from (e.g., 'USD').
        to_currency (str): The currency code to convert to (e.g., 'EUR').

    Returns:
        float: The converted amount in the target currency.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    if not api_key:
        raise ValueError("ALPHA_VANTAGE_API_KEY environment variable is not set.")
    
    alpha_vantage = AlphaVantageAPIWrapper()
    response = alpha_vantage._get_exchange_rate(from_currency,to_currency)
    exchange_rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
    converted_amount = amount * float(exchange_rate)
    
    return converted_amount