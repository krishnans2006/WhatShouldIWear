from flask import Flask, request, render_template, redirect, url_for, session

import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.route("/") 
def index():
  no_loc_available = True
  try:
    lat, lng = session["lat"], session["lng"]
    no_loc_available = False
  except:
    lat, lng = 9.5127, 122.8797
  data_now = json.loads(requests.get("http://api.weatherapi.com/v1/current.json?key={0}&q={1},{2}".format(os.getenv("WEATHERAPI_KEY"), lat, lng)).content)
  factors = { "rain": None}
  if data_now["current"]["precip_mm"] > 0:
    factors["rain"] = True
  if data_now["current"]["feelslike_f"] > 80:
    factors["clothing"] = "Shorts"
  elif data_now["current"]["feelslike_f"] > 65:
    factors["clothing"] = "T-Shirt"
  elif data_now["current"]["feelslike_f"] > 45:
    factors["clothing"] = "Long Sleeve"
  elif data_now["current"]["feelslike_f"] > 25:
    factors["clothing"] = "Sweater"
  else:
    factors["clothing"] = "Jacket"
  sentence = "Wear a {0}".format(factors["clothing"]) + (" and keep an umbrella handy" if factors["rain"] else "")
  return render_template("index.html", data=data_now, sentence=sentence, nlc=no_loc_available)

@app.route("/save_location", methods=["POST"])
def save_location():
  data = request.get_json()
  session["lat"] = data["lat"]
  session["lng"] = data["lng"]
  print("Saved!")
  return redirect(url_for("index"))
  

if __name__ == "__main__":
  app.run()

# API JSON Format
# {
# 	u'current': {
# 		u'gust_kph': 15.8, 
# 		u'last_updated': u'2020-09-12 22:15', 
# 		u'vis_miles': 9.0, 
# 		u'pressure_in': 30.7, 
# 		u'cloud': 0, 
# 		u'precip_mm': 0.0, 
# 		u'is_day': 0, 
# 		u'feelslike_c': 20.0, 
# 		u'condition': {
# 			u'text': u'Clear', 
# 			u'code': 1000, 
# 			u'icon': u'//cdn.weatherapi.com/weather/64x64/night/113.png'
# 		}, 
# 		u'feelslike_f': 68.0, 
# 		u'wind_mph': 8.1, 
# 		u'temp_f': 68.0, 
# 		u'temp_c': 20.0, 
# 		u'last_updated_epoch': 1599963306, 
# 		u'pressure_mb': 1024.0, 
# 		u'vis_km': 16.0, 
# 		u'precip_in': 0.0, 
# 		u'wind_dir': u'E', 
# 		u'wind_kph': 13.0, 
# 		u'uv': 1.0, 
# 		u'humidity': 73, 
# 		u'gust_mph': 9.8, 
# 		u'wind_degree': 100
# 	}, 
# 	u'location': {
# 		u'name': u'Foxhall', 
# 		u'country': u'United States of America', 
# 		u'region': u'Virginia', 
# 		u'tz_id': u'America/New_York', 
# 		u'lon': -77.18, 
# 		u'lat': 38.91, 
# 		u'localtime_epoch': 1599963346, 
# 		u'localtime': u'2020-09-12 22:15'
# 	}
# }