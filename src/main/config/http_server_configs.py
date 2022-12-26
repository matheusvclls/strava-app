from fastapi import FastAPI
from src.main.routes import strava_routes

app = FastAPI()

app.include_router(strava_routes)