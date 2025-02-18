"""
File: sm_api_requests.py
Author: Andrew Silkwood
Date Created: 2025-02-15
Description:
    A bridge to connect the bot code to a stock market API.
    Currently configured for Tiingo API.
"""

from datetime import date
import os

from dotenv import load_dotenv
import requests

# Global Variables
# .env vars
load_dotenv()
API_TOKEN = os.getenv("SM_API_TOKEN")
API_URL = os.getenv("SM_API_URL")


# Get current information about a ticker
def eod_ticker(ticker: str):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {API_TOKEN}",
    }
    response = requests.get(f"{API_URL}/tiingo/daily/{ticker}/prices", headers=headers)
    return response.json()


# Get information about a ticker for specified amount of years
def eod_ticker_year(ticker: str, years: int):
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
def eod_ticker_desc(ticker: str):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {API_TOKEN}",
    }
    response = requests.get(f"{API_URL}/tiingo/daily/{ticker}", headers=headers)
    return response.json()


# Searches for tickers based on a query
def search_query(query: str):
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
