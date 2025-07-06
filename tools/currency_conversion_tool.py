import os
from utils.currency_converter_tool import CurrencyConverter
from dotenv import load_dotenv
from typing import List
from langchain.tools import tool



class CurrencyConverter:
    def __init__(self):
        self.api_key = os.getenv("EXCHANGE_RATE_API_KEY")
        self.currency_service = CurrencyConverter(api_key=self.api_key)
        self.currency_converter_tool_list = self._setup_tools()
    
    def _setup_tools(self) -> List[tool]:
        """Setup all tools for the currency converter tool"""

        @tool
        def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
            """Convert currency from one to another"""
            return self.currency_service.convert_currency(amount, from_currency, to_currency)
        
        return [convert_currency]

