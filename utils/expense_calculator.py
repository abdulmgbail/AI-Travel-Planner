class Calculator:

    @staticmethod
    def multiply(a: int, b: int):
        """Multiplies two numbers."""
        return a * b

    @staticmethod
    def calculate_total(*x:float):
        """
            Calculates the sum of given numbers.
            Args:
                *x (float): Variable number of float arguments.
            Returns:
                float: The total sum of the provided numbers.
        """
        return sum(x)
    
    @staticmethod
    def calculate_daily_budget(total_budget: float, days: int) -> float:
        """
        Calculates the daily budget based on total budget and number of days.
        
        Args:
            total_budget (float): The total budget available.
            days (int): The number of days for the trip.
        
        Returns:
            float: The daily budget.
        """
        
        return total_budget / days if days > 0 else 0
