# SkyCast — Real-Time Weather Visualizer & Predictor

SkyCast is a Python-based weather application that transforms real-time weather data into dynamic visual scenes. It combines live API integration, data analytics, simple prediction logic, and graphics-based rendering to create an interactive weather experience.

Built as a final project for **Stanford Code in Place, 2026**, this project demonstrates how code can turn raw data into meaningful and visual storytelling.

---

## Features

- Real-time weather data using OpenWeatherMap API  
- Dynamic weather scenes (Sunny, Rainy, Cloudy, Thunderstorm)  
- Graphics-based visualization using Pygame  
- Basic weather analytics (trend insights, averages, patterns)  
- Simple prediction logic based on past weather patterns  
- Clean modular Python structure  

---

## How It Works

1. User enters a city name  
2. App fetches live weather data from OpenWeatherMap API  
3. Weather condition is parsed (Clear, Rain, Clouds, etc.)  
4. Matching visual scene is displayed using Pygame  
5. Data is stored for analytics and prediction  
6. System generates simple weather trend insights  

---

## Weather Visuals

- **Sunny Scene** → Bright sky with sun animation  
- **Rainy Scene** → Falling rain animation  
- **Cloudy Scene** → Moving cloud visuals  
- **Thunderstorm Scene** → Flashing lightning effect  

---

## Analytics

SkyCast tracks user queries and weather patterns to provide:

- Average temperature trends  
- Most frequent weather condition  
- Basic distribution of weather types  

---

## Prediction Logic

The system uses simple frequency-based analysis:

- More rain occurrences → predicts rainy trend  
- More clear skies → predicts sunny trend  
- Mixed data → predicts unstable weather  

---

## Tech Stack

- Python  
- Requests (API calls)  
- Pygame (Graphics & animation)  
- OpenWeatherMap API  

---

## How to Run

```bash
pip install requests pygame
python main.py