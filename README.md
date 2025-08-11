# 🌦 Weather Checker Website (Python + HTML)

This project is a **Weather Website** built with **Python** and **HTML** that allows users to check the **current weather** by entering a **country name** and **city name**.  
It uses a weather API to fetch live data and display it on the webpage.

---

## 📂 Project Structure

weather-website/
│
├── main.py # Python backend to handle weather API requests
├── index.html # Frontend HTML file for user interface
├── map.jpg # Map image used in the website
├── .venv/ # Virtual environment (excluded from GitHub)
├── pycache/ # Python cache files (excluded from GitHub)
├── README.md # Project documentation 


---

## 🚀 Features

- 🌍 Search weather by **country name** and **city name**  
- ☀ Shows temperature, humidity, wind speed, and weather description  
- 🖼 Includes a map image for design enhancement  
- 🔄 Fetches **real-time data** from an API  
- 🎨 HTML interface with Python backend

---

## 🛠 Technologies Used

- **Python** (Flask or similar for backend)  
- **HTML** (Frontend interface)  
- **Requests library** (for API calls)  
- **OpenWeatherMap API** (or other API)  
- **map.jpg** (image for UI)

---

## 📖 How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/weather-website.git
cd weather-website

##2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # For Mac/Linux
.venv\Scripts\activate      # For Windows

##3. Install dependencies
pip install requests flask

##4. Add your API key
Sign up at OpenWeatherMap to get a free API key.
In main.py, replace:
api_key = "YOUR_API_KEY"

##5. Run the app
python main.py

##6. Open in browser
http://127.0.0.1:5000

##📌 Notes
.venv and __pycache__ are excluded from this repository to keep it clean.
 The project requires internet access to fetch weather data.

##👤 Author
areebaahmed2 

