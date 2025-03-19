
"""
Discuss and potentially design a system that incorporates external economic factors (like inflation rates, economic downturns, etc.) to adjust the forecasts more dynamically. This could involve accessing external APIs for real-time data, processing it, and integrating it into the forecasting logic
"""
import json
import requests
from dotenv import load_dotenv
import os
from datetime import datetime
from part_2 import part_2
from groq import Groq

load_dotenv()
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
ALPHA_VANTAGE_API_URL = os.getenv("ALPHA_VANTAGE_API_URL")
API_NINJA_API_KEY     = os.getenv("API_NINJA_API_KEY")
API_NINJA_API_URL     = os.getenv("API_NINJA_API_URL")
GROQ_API_KEY          = os.getenv("GROQ_API_KEY")

def _interpret_news(expenses: dict, news: list[str]) -> str:
  if not GROQ_API_KEY:
    raise ValueError(".env file not found or API keys are not set")
  client = Groq(api_key=GROQ_API_KEY)
  response = client.chat.completions.create(
    messages=[
      {
        "role": "system",
        "content": f"ONLY OUTPUT JSON. You are a financial analyst at Intuit, analyzing macroeconomic news for potential impacts on the forcasted monthly expenses shown between <<<>>> \n <<< {json.dumps(expenses)} >>> \n TASK: Give only a single sentence response and cite source on why you think there is an expected increase or decrease of each category of expenses. return ONLY JSON with categories as keys and your answer as value."
      },
      {
        "role": "user",
        "content": "~".join(summary for summary in news),
      }
    ],
    model="llama-3.3-70b-versatile",
    temperature=1.0,
    max_tokens=8000,
    top_p=1,
  )
  return response.choices[0].message.content


def call_api(
    type: str,
    country: str,
  ) -> dict:
  url: str = ""
  headers: dict = {}
  response: requests.Response = None
  # calculate the beginning of the current month
  now: datetime= datetime.now()
  beginning_of_month: datetime = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
  first_of_curr_month: str = beginning_of_month.strftime("%Y%m%dT%H%M")

  if ( not ALPHA_VANTAGE_API_KEY or not ALPHA_VANTAGE_API_URL
      or not API_NINJA_API_KEY or not API_NINJA_API_URL):
    raise ValueError(".env file not found or API keys are not set")

  API_LIST: dict = {
    "API_ninja": {
      "inflation": API_NINJA_API_URL.rstrip('\"') + "inflation?country=" + country,
    },
    "ALPHA_vantage": {
      "macro_economy": ALPHA_VANTAGE_API_URL + "NEWS_SENTIMENT"
        + "&topics=" + "economy_macro"
        + "&time_from=" + first_of_curr_month
        + "&limit=" + "5"
        + "&apikey=" + ALPHA_VANTAGE_API_KEY
    }
  }

  # choose the API based on the the requested info
  if type == "inflation":
    url = API_LIST["API_ninja"]["inflation"]
    headers = {'X-Api-Key': API_NINJA_API_KEY}
  elif type == "macro_economy":
    url = API_LIST["ALPHA_vantage"]["macro_economy"]

  try:
    response = requests.get(url, headers=headers)
  except Exception as e:
    print("Error fetching data:", e)
    print(response.status_code, response.text)

  return response.json()

def _get_current_inflation_data(country: str) -> list[dict]:
  return call_api('inflation', country)

def _get_ai_input(expenses: dict, country: str) -> dict:
  news: dict = call_api('macro_economy', country)
  # extract the summaries, if free api tokens run out, this will be empty
  summaries: list[str] = []
  for news_item in news.get("feed", []):
    summaries.append(news_item["summary"])
  # feed the summaries to the AI model and return the result
  return json.loads(_interpret_news(expenses, news))

def forecast_next_expenses_weighted_with_external_factors(
    debug: bool,
    expense_data: list,
    period: int,
    country: str
  ) -> dict:
  """
  forecast expenses for the next month using a weighted moving average and external factors.
  Args:
    expense_data (dict[str, list]): Historical expense data for each category
    period (int): Number of months to consider for the moving average
    country (str): Country to get external economic data for
  Returns:
    dict: forecasted next month expenses for each category
  """

  result: dict = {}
  # calculate WMA
  expenses_WMA_3_months = part_2.forecast_next_expenses_weighted(debug, expense_data, period)
  # adjust WMA based on external factors (current inflation rate)
  inflation_rate: float = _get_current_inflation_data(country)[0].get("monthly_rate_pct")
  # get macroeconomic news and feed to the AI model
  LLM_tips: dict = _get_ai_input(expense_data, country)

  for category in expenses_WMA_3_months:
    result[category] = {
      f"WMA + {inflation_rate}% CPI": round(expenses_WMA_3_months[category] * (1 + inflation_rate / 100)),
      "LLM Suggestion": LLM_tips[category]
    }

  if debug:
    inflation = _get_current_inflation_data(country)
    print("Inflation Data:", json.dumps(inflation, indent=2))
    print("inflation_rate:", inflation[0].get("monthly_rate_pct"))

  return result