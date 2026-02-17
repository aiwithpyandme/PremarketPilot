# main.py

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from pathlib import Path

# -------------------------------
# App initialization
# -------------------------------
app = FastAPI(title="PremarketPilot", description="Pre-market trading prep dashboard")

# -------------------------------
# Template configuration
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent  # absolute path to project folder
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# -------------------------------
# Sample in-memory data (replace with DB later)
# -------------------------------
sample_gappers = [
    {"symbol": "AAPL", "gap": 2.5, "volume": 100000},
    {"symbol": "TSLA", "gap": 3.1, "volume": 150000},
]

sample_volume_spikes = [
    {"symbol": "NVDA", "change": 5.0, "volume": 500000},
    {"symbol": "AMZN", "change": 4.2, "volume": 300000},
]

# -------------------------------
# Routes
# -------------------------------

@app.get("/")
def dashboard(request: Request):
    """
    Render the main dashboard page.
    """
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "gappers": sample_gappers,
            "volume_spikes": sample_volume_spikes
        }
    )

@app.get("/premarket")
def premarket_data():
    """
    Return JSON data for premarket gappers and volume spikes.
    Can be used for API calls or AJAX frontend updates.
    """
    return JSONResponse(
        {
            "gappers": sample_gappers,
            "volume_spikes": sample_volume_spikes
        }
    )

# -------------------------------
# Optional health check
# -------------------------------
@app.get("/health")
def health_check():
    return {"status": "ok"}

# -------------------------------
# Run locally: uvicorn main:app --reload
# On Render, Uvicorn runs automatically
# -------------------------------
