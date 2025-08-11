# from fastapi import FastAPI, HTTPException
# import httpx  # Replacing requests with httpx

# app = FastAPI()

# API_KEY = "5e7c1f10f03720d98b263af62cbd087d"
# BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# @app.get("/weather/{city}")
# async def get_weather(city: str):
#     url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"  # Added units=metric for Celsius

#     async with httpx.AsyncClient() as client:
#         response = await client.get(url)  # Asynchronous request
    
#     if response.status_code == 200:
#         data = response.json()
#         return {
#             "city": data.get("name", "Unknown"),
#             "temperature": data["main"].get("temp", 0),  # Temperature in Celsius
#             "weather": data["weather"][0].get("description", "No data"),
#             "humidity": data["main"].get("humidity", 0)
#         }
    
#     raise HTTPException(status_code=response.status_code, detail="City not found")
# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# import httpx  

# app = FastAPI()

# # Allow frontend requests from any origin (CORS fix)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allow requests from any frontend
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# API_KEY = "5e7c1f10f03720d98b263af62cbd087d"
# BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# @app.get("/weather/{city}")
# async def get_weather(city: str):
#     url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

#     async with httpx.AsyncClient() as client:
#         response = await client.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         return {
#             "city": data.get("name", "Unknown"),
#             "temperature": data["main"].get("temp", 0),
#             "weather": data["weather"][0].get("description", "No data"),
#             "humidity": data["main"].get("humidity", 0)
#         }
    
#     raise HTTPException(status_code=response.status_code, detail="City not found")

 


from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx  

app = FastAPI()

# Allow frontend requests from any origin (CORS fix)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "5e7c1f10f03720d98b263af62cbd087d"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.get("/weather/{city}")
async def get_weather(city: str):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "city": data.get("name", "Unknown"),
            "temperature": data["main"].get("temp", 0),
            "weather": data["weather"][0].get("description", "No data"),
            "humidity": data["main"].get("humidity", 0),
            "wind_speed": data["wind"].get("speed", 0),
            "pressure": data["main"].get("pressure", 0),
            "icon": data["weather"][0].get("icon", "01d"),
        }
    
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="City not found. Please check the spelling.")
    
    raise HTTPException(status_code=response.status_code, detail="Failed to fetch weather data. Try again later.")
# from fastapi import FastAPI, HTTPException