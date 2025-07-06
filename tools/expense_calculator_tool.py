from typing import List
from langchain.tools import tool
from utils.expense_calculator import Calculator

class ExpenseCalculatorTool:

    def __init__(self):
        self.calculator = Calculator()
        self.calculator_tool_list = self._setup_tools()

    def _setup_tools(self) -> List[tool]:
        """Setup all tools for the expense calculator tool"""

        @tool
        def estimate_total_hotel_cost(price_per_night:str , total_days: int) -> float:
            """Calculate total hotel cost"""
            return self.calculator.multiply(price_per_night, total_days)
        
        @tool
        def calculate_total_expenses(*costs: float) -> float:
            """Calculate total expenses from a list of expenses"""
            return self.calculator.calculate_total(*costs)
        
        @tool
        def calculate_daily_budget(total_cost: float, days: int) -> float:
            """Calculate daily budget based on total budget and number of days"""
            return self.calculator.calculate_daily_budget(total_cost, days)

        return [estimate_total_hotel_cost, calculate_total_expenses, calculate_daily_budget]
        


    