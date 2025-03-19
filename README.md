# Intuit Case 2 Solution

## By: Devon Knight, 2025-03-19

### Instructions
Using Windows Subsystem fo rLinux, Linux, or OSX
```bash
# unzip file
unzip intuit_case_2.zip

# build docker image
docker build -t intuit-case-2

# run docker image
docker run intuit-case-2

# EXPECTED OUTPUT BELOW
```
**NOTE**: For Part 3, API keys will be used during online interview on Friday

**NOTE**: This will use `docker run --env-file .env intuit-case-2`
```
###############################################################################
PART 1: Simple moving average of the last three months
###############################################################################
{
  "Office Supplies": 140,
  "Marketing": 220,
  "Utilities": 92,
  "Rent": 1000
}
###############################################################################
PART 2: Weighted average of the last three months
###############################################################################
{
  "Office Supplies": 138,
  "Marketing": 222,
  "Utilities": 90,
  "Rent": 1000
}
###############################################################################
PART 3: Forecast expenses and incorporate external economic factors (API's)
###############################################################################
Traceback (most recent call last):
  File "/app/main.py", line 70, in <module>
    run_part_3()
  File "/app/main.py", line 58, in run_part_3
    print(json.dumps(part_3.forecast_next_expenses_weighted_with_external_factors(
  File "/app/part_3/part_3.py", line 119, in forecast_next_expenses_weighted_with_external_factors
    inflation_rate: float = _get_current_inflation_data(country)[0].get("monthly_rate_pct")
  File "/app/part_3/part_3.py", line 88, in _get_current_inflation_data
    return call_api('inflation', country)
  File "/app/part_3/part_3.py", line 57, in call_api
    raise ValueError(".env file not found or API keys are not set")
ValueError: .env file not found or API keys are not set
```
