from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Point to templates folder
templates = Jinja2Templates(directory="templates")

# Serve static files like CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def dashboard(request: Request):
    gappers = [
        {"symbol":"AAPL","gap":2.5,"volume":100000},
        {"symbol":"TSLA","gap":3.1,"volume":150000}
    ]
    volume_spikes = [
        {"symbol":"NVDA","change":5.0,"volume":500000},
        {"symbol":"AMZN","change":4.2,"volume":300000}
    ]
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "gappers": gappers,
        "volume_spikes": volume_spikes
    })
