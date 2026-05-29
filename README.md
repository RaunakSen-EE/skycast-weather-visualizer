# SkyCast — Real-Time Weather Visualizer

SkyCast is a Python-based weather application that transforms real-time weather data into dynamic visual scenes. It combines live API integration, graph visualization, analytics display, and graphics-based rendering to create an interactive weather experience.

Built as a final project for Stanford Code in Place, 2026, this project demonstrates how code can turn real-time weather data into engaging visual simulations using Python and Pygame.

---

## Features

* Real-time weather data using OpenWeatherMap API
* Dynamic weather scenes (Sunny, Rainy, Cloudy, Thunderstorm)
* Graphics-based visualization using Pygame
* Analytics dashboard with graph integration
* Temperature graph visualization using Matplotlib
* Clean modular Python structure

---

## How It Works

1. User enters a city name
2. App fetches live weather data from OpenWeatherMap API
3. Weather condition is parsed (Clear, Rain, Clouds, etc.)
4. Matching visual scene is displayed using Pygame
5. Temperature graph is generated dynamically
6. Analytics dashboard is rendered inside the application

---

## Weather Visuals

* **Sunny Scene** → Bright sky with animated sun effect
* **Rainy Scene** → Moving clouds with falling rain animation
* **Cloudy Scene** → Animated drifting cloud visuals
* **Thunderstorm Scene** → Flashing lightning storm effect

---

## Analytics Dashboard

SkyCast includes a lightweight analytics dashboard inside the Pygame window:

* Temperature graph visualization
* Weather analytics panel
* Dynamic graph rendering using Matplotlib

---

## Tech Stack

* Python
* Requests (API calls)
* Pygame (Graphics & animation)
* Matplotlib (Graph generation)
* OpenWeatherMap API

---

## Project Structure

```text
skycast-weather-visualizer/
│
├── main.py
├── scenes.py
├── weather_api.py
├── graph_generator.py
├── README.md
└── .gitignore
```

---

## How to Run

```bash
pip install requests pygame matplotlib
python main.py
```

---

## Future Improvements

* Sound effects for weather scenes
* Multi-city analytics tracking
* Forecast support
* Improved UI transitions
* Expanded weather condition support

---
