# SkyCast — Real-Time Weather Visualizer

SkyCast is a Python-based weather application that combines real-time weather data, interactive visualizations, animated weather scenes, and a web interface into a single project.

Built as a final project for Stanford Code in Place, SkyCast demonstrates API integration, data visualization, graphics programming, web development, and modular software design using Python.

---

## Overview

SkyCast allows users to enter a city name and instantly retrieve live weather information using the OpenWeatherMap API. The application can display weather information through:

* A Flask-based web interface
* Animated weather visualizations using Pygame
* Temperature trend graphs using Matplotlib
* Real-time weather analytics

---

## Features

### Real-Time Weather Data

* Fetches live weather information using the OpenWeatherMap API
* Displays:

  * City Name
  * Weather Condition
  * Temperature
  * Humidity

### Animated Weather Visualizations

SkyCast automatically displays different animated scenes based on current weather conditions:

* ☀️ Sunny Scene
* 🌧️ Rainy Scene
* ☁️ Cloudy Scene
* 🌩️ Thunderstorm Scene

### Analytics Dashboard

* Temperature graph generation
* Weather analytics display
* Dynamic graph rendering using Matplotlib

### Web Interface

* Clean Flask-powered user interface
* Responsive weather search form
* Easy-to-use weather dashboard

---

## Technologies Used

* Python
* Flask
* Requests
* Pygame
* Matplotlib
* HTML
* CSS
* OpenWeatherMap API

---

## Project Structure

```text
SkyCast/
│
├── app.py
├── main.py
├── weather_api.py
├── graph_generator.py
├── scenes.py
├── config.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## How It Works

### Desktop Visualization Mode

1. User enters a city name
2. Weather data is fetched from OpenWeatherMap
3. Weather condition is analyzed
4. Temperature graph is generated
5. Appropriate animated weather scene is displayed

### Web Application Mode

1. User opens the Flask application
2. Enters a city name
3. Weather data is fetched in real time
4. Results are displayed in a clean web dashboard

---

## API Setup

This project requires an OpenWeatherMap API key.

### Step 1: Create a Free Account

Visit:

https://openweathermap.org/

Create a free account and log in.

### Step 2: Generate an API Key

Navigate to:

API Keys → Generate New Key

Copy your API key.

### Step 3: Create config.py

Create a file named:

```python
config.py
```

Add:

```python
API_KEY = "YOUR_OPENWEATHER_API_KEY"
```

Example:

```python
API_KEY = "abcd1234yourapikey"
```

### Important

Do not commit your API key to GitHub.

Your `.gitignore` should contain:

```text
config.py
```

This prevents your private API key from being uploaded publicly.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd SkyCast
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install flask requests pygame matplotlib
```

---

## Running the Project

### Run the Flask Web Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

### Run the Desktop Visualization Version

```bash
python main.py
```

Enter a city name when prompted.

The application will:

* Fetch live weather data
* Generate a temperature graph
* Display an animated weather scene

Press ESC to close the visualization window.

---

## Example Output

Weather Report:

```text
City: Kolkata
Weather: Clouds
Temperature: 31°C
Humidity: 70%
```

The application then generates:

* Temperature graph
* Weather analytics dashboard
* Animated weather visualization

---

## Future Improvements

* Multi-city weather comparison
* Historical weather tracking
* Forecast support
* Weather alerts
* Sound effects
* Enhanced dashboard analytics
* Database integration
* Mobile-friendly web interface

---

## Learning Outcomes

This project demonstrates:

* API Integration
* JSON Data Processing
* Flask Web Development
* Pygame Graphics Programming
* Data Visualization
* Modular Python Design
* User Interface Development
* Software Project Organization

---

## Author

Raunak Sen

Built as part of the Stanford Code in Place learning journey using Python, APIs, data visualization, graphics programming, and web technologies.
