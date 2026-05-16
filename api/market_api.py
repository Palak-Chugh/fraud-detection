#uvicorn api.market_api:app --reload
from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/market-rates/{sector}")

def get_market_rates(sector: str):

    return {
        "sector": sector,
        "interest_rate": round(
            random.uniform(4.0, 11.0),
            2
        )
    }