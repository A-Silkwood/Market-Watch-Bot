from utils import JSONType
from dotenv import load_dotenv
import os
from datetime import date
import requests

# Global Variables
# .env vars
load_dotenv()
API_TOKEN = os.getenv("SM_API_TOKEN")
API_URL = os.getenv("SM_API_URL")


def main():
    print(search_query("google"))


# Get current information about a ticker
def eod_ticker(ticker: str) -> JSONType:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {API_TOKEN}",
    }
    response = requests.get(f"{API_URL}/tiingo/daily/{ticker}/prices", headers=headers)
    return response.json()


# Get information about a ticker for specified amount of years
def eod_ticker_year(ticker: str, years: int) -> JSONType:
    years = 1 if years < 1 else years

    d = date.today()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {API_TOKEN}",
    }
    params = {
        "startDate": d.replace(year=d.year - years).isoformat(),
        "resampleFreq": "monthly" if years > 1 else "weekly",
        "sort": "date",
    }
    response = requests.get(
        f"{API_URL}/tiingo/daily/{ticker}/prices", headers=headers, params=params
    )
    return response.json()


# Get detail information about a ticker
def eod_ticker_desc(ticker):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {API_TOKEN}",
    }
    response = requests.get(f"{API_URL}/tiingo/daily/{ticker}", headers=headers)
    return response.json()


# Don't have access
# def news_ticker(ticker):
#     d = date.today()

#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Token {API_TOKEN}",
#     }
#     params = {
#         "startDate": d.replace(month=d.month - 1).isoformat(),
#         "limit": 50,
#     }
#     response = requests.get(f"{API_URL}/tiingo/news", headers=headers, params=params)
#     return response.json()


# Don't have access
# def dist_ticker(ticker):
#     d = date.today()

#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Token {API_TOKEN}",
#     }
#     response = requests.get(
#         f"{API_URL}/tiingo/corporate-actions/{ticker}/distributions", headers=headers
#     )
#     return response.json()


# Searches for tickers based on a query
def search_query(query):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {API_TOKEN}",
    }
    params = {
        "query": query,
    }
    response = requests.get(
        f"{API_URL}/tiingo/utilities/search", headers=headers, params=params
    )
    return response.json()


if __name__ == "__main__":
    main()
