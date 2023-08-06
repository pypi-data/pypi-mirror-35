from flask import Flask, render_template, jsonify
app = Flask(__name__)
 
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/calendar")
def getCalendar():
    return render_template('calendar.html')

@app.route("/weather/<city>")
def getWeather(city):
    import geocoder
    g = geocoder.ip('me')
    print(g.latlng)

    from weather import Weather, Unit
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location(city)
    # print(location.print_obj)
    # print(condition.text)
    # return jsonify(location.print_obj)
    # location.astronomy
    # print("Temp:", location.item['description'])
    # print("Condition:", location.condition.text)
    # print(location.forecast[0].text)

    if(location):
        weatherDetails = {
            "City": location.location.city,
            "State": location.location.region,
            "Country": location.location.country,
            "Sunrise": location.astronomy['sunrise'],
            "Sunset": location.astronomy['sunset'],
            "Humidity": location.atmosphere['humidity'],
            "Temp": location.condition.temp,
            "Condition": location.condition.text
        }
        return render_template('weather.html', weather=weatherDetails)
    return ""
    # return jsonify(location.print_obj)
    # return location.forecast

if __name__ == "__main__":
    # app.run(ssl_context='adhoc')
    app.run(port=5000)