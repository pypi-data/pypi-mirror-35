from flask import Flask, render_template, jsonify
from smart_mirror import app

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/calendar")
def getCalendar():
    return render_template('calendar.html')

@app.route("/news")
def getNews():
    import bs4
    from bs4 import BeautifulSoup as soup
    from urllib.request import urlopen

    news_url="https://news.google.com/news/rss"
    Client=urlopen(news_url)
    xml_page=Client.read()
    Client.close()

    soup_page=soup(xml_page,"xml")
    news_list=soup_page.findAll("item")
    # Print news title, url and publish date
    for news in news_list:
        print(news.title.text)
        print(news.link.text)
        print(news.pubDate.text)
        print("-"*60)

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

# def main():
#     app.run(port=5000)