from flask import Flask, jsonify

app = Flask(__name__)

# Sample weather data
weather_data = {
    "city": "New York",
    "temperature": 20,
    "humidity": 65,
    "wind_speed": 10,
    "description": "Cloudy"
}

# Endpoint to get current weather
@app.route('/weather', methods=['GET'])
def get_weather():
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
