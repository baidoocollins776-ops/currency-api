from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
import requests

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    html_file = Path("templates/index.html")
    return html_file.read_text()


@app.get("/convert")
def convert(from_currency: str, to_currency: str, amount: float):

    url = f"https://open.er-api.com/v6/latest/{from_currency}"

    response = requests.get(url)

    data = response.json()

    rate = data["rates"][to_currency]

    converted_amount = amount * rate

    return {
        "from_currency": from_currency,
        "to_currency": to_currency,
        "amount": amount,
        "exchange_rate": rate,
        "converted_amount": round(converted_amount, 2)
    }