from flask import Flask, render_template, request
from weather_api import get_weather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    weather_data = None

    if request.method == "POST":

        city = request.form["city"]

        weather_data = get_weather(city)

    return render_template(
        "index.html",
        weather=weather_data
    )

if __name__ == "__main__":
    app.run(debug=True)