"""
Part 2:
Enhance the forecasting model by introducing weighted averages where more recent months are given higher importance. Adjust your function to calculate a weighted average for forecastions.
"""

def weighted_moving_average(debug: bool, data: list, period: int) -> int:
  """
  Compute the weighted moving average of a given time series using linear weights.
  Args:
    data (list): List of numbers
    period (int): Number of elements to consider for the average
  Returns:
    int: Weighted moving average of the last `period` elements in the list
  """
  if len(data) < period or period < 1:
    raise ValueError("Data length cannot be less than the period.")
  if period == None:
    period = len(data)

  weights: list = []
  total_weight: int = 0
  weighted_sum: int = 0

  for i in range(1, period+1):
    weights.append(i)
    total_weight += i

  for i in range(period):
    weighted_sum += data[-period + i] * weights[i]
    if debug:
      print("Data point = ", data[-period + i], "\t | assigned weight =", weights[i])

  if debug:
    print("weighted_sum = ", weighted_sum, "\t | total_weight = ", total_weight)

  return round(weighted_sum / total_weight)

def forecast_next_expenses_weighted(debug: bool, expense_data: list, period: int) -> dict:
  """
  forecast expenses for the next month using a weighted moving average.
  Args:
    expense_data (dict[str, list]): Historical expense data for each category
    period (int): Number of months to consider for the moving average
  Returns:
    dict: forecasted next month expenses for each category
  """
  result: dict = {}
  for category, expenses in expense_data.items():
    result[category] = weighted_moving_average(debug, expenses, period)
  return result