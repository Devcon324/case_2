"""
Expense Forecasting System
"""
import json
from part_1 import part_1
from part_2 import part_2
from part_3 import part_3
from dotenv import load_dotenv
load_dotenv()

#************* Assumptions *************
#* Assuming the data is not empty
#* Assuming the most recent months reside at the end of the list
#* Assuming the data is in the same order for all categories
#* Assuming all forecasts (part 1,2,3) are based the last three months
#* Assuming the outputs should be integers rounded to nearest whole number

DEBUG = False # for added explanation
expense_data = {
  "Office Supplies": [120, 110, 150, 130, 140],
  "Marketing": [200, 240, 220, 210, 230],
  "Utilities": [90, 95, 100, 85, 90],
  "Rent": [1000, 1000, 1000, 1000, 1000]
}

def run_part_1():
  print(""
  "###############################################################################"
  "\nPART 1: Simple moving average of the last three months\n"
  "###############################################################################"
  "")
  print(json.dumps(part_1.forecast_next_expenses(
      debug=DEBUG,
      expense_data=expense_data,
      period=3),
    indent=2
  ))

def run_part_2():
  print(""
  "###############################################################################"
  "\nPART 2: Weighted average of the last three months\n"
  "###############################################################################"
  "")
  print(json.dumps(part_2.forecast_next_expenses_weighted(
      debug=DEBUG,
      expense_data=expense_data,
      period=3),
    indent=2
  ))

def run_part_3():
  print(""
  "###############################################################################"
  "\nPART 3: Forecast expenses and incorporate external economic factors (API's)\n"
  "###############################################################################"
  "")
  print(json.dumps(part_3.forecast_next_expenses_weighted_with_external_factors(
      debug=DEBUG,
      expense_data=expense_data,
      period=3,
      country="Switzerland"),
    indent=2
  ))

if __name__ == "__main__":
  print("RAH")
  run_part_1()
  run_part_2()
  run_part_3()