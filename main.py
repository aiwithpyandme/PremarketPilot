from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()

# Serve static files (CSS/JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="templates")

# Frontend route
@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

# API endpoint
@app.get("/premarket")
def get_premarket():
    # Sample data for MVP
    data = {
        "gappers": ["AAPL", "TSLA", "NVDA"],
        "volume_spikes": ["AMD", "META"]
    }
    return JSONResponse(content=data)
