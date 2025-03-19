"""
Expense Forecasting System

Scenario: You are part of a team at Intuit working on an advanced feature for QuickBooks that helps small business owners forecast future expenses based on historical data. The goal is to provide forecastive insights that can help businesses better manage their budgets and plan for future financial needs.

Instructions: Write a function in your preferred programming language that takes `expense_data` as input and returns forecasted expenses for each category using a simple moving average of the last three months.

Initial Task (Part 1): Implement a function that analyzes historical expense data and forecasts the next months expenses for various categories. You are given a list of past monthly expenses for several categories.

Input:
expense_data = {
  "Office Supplies": [120, 110, 150, 130, 140],
  "Marketing": [200, 240, 220, 210, 230],
  "Utilities": [90, 95, 100, 85, 90],
  "Rent": [1000, 1000, 1000, 1000, 1000]
}

Expected Output: A dictionary with categories as keys and forecasted expenses for the next month as values.
{
  "Office Supplies": 135,
  "Marketing": 225,
  "Utilities": 92,
  "Rent": 1000
}
"""

def _simple_moving_average(debug: bool, data: list, period: int) -> int:
  """
  Calculate the simple moving average of a list of numbers.
  Args:
    data (list): List of numbers
    period (int): Number of elements to consider for the average
  Returns:
    int: Simple moving average of the last `period` elements in the list
  """
  if debug: print(data[-period:], sum(data[-period:]) / period)
  return round(sum(data[-period:]) / period)

def forecast_next_expenses(debug: bool, expense_data: dict[str, list], period: int) -> dict:
  """
  forecast expenses for the next month using a simple moving average.
  Args:
    expense_data (dict[str, list]): Historical expense data for each category
    period (int): Number of months to consider for the moving average
  Returns:
    dict: forecasted next month expenses for each category
  """
  # I can calculate the average of the last three months
  result: dict = {}
  for category, expenses in expense_data.items():
    result[category] = _simple_moving_average(debug, expenses, period)
  return result