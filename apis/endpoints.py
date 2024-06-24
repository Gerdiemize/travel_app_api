from fastapi import APIRouter, HTTPException
from .api_functions import get_events_near
from .api_functions import get_current_weather_conditions

router = APIRouter()

@router.get("/events")
async def events_near(latitude: float, longitude: float, keyword: str, start_date_time: str = None, end_date_time: str = None):
    try:
        events = get_events_near(latitude, longitude, keyword, start_date_time, end_date_time)
        return events
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/weather")
async def weather_conditions(latitude: float, longitude: float):
    try:
        weather = get_current_weather_conditions(latitude, longitude)
        return weather
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
