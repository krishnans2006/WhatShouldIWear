# THE CODE IS SO SPAGHETTI IT HAS STARTED SPEAKING ITALIAN
from flask import Flask, request, render_template, redirect, url_for, jsonify, session

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
  data_now = json.loads(requests.get("http://api.weatherapi.com/v1/current.json?key=83fd32f4726d43e8bc320912201309&q={0},{1}".format(lat, lng)).content)
  factors = { "rain": None}
  if data_now["current"]["precip_mm"] > 0:
    factors["rain"] = True
  if data_now["current"]["temp_f"] > 80:
    factors["clothing"] = "Shorts"
  elif data_now["current"]["temp_f"] > 65:
    factors["clothing"] = "T-Shirt"
  elif data_now["current"]["temp_f"] > 45:
    factors["clothing"] = "Long Sleeve"
  elif data_now["current"]["temp_f"] > 25:
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