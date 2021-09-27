from flask import Flask, render_template
import requests
import json

def get_data(city):
    appid = "392b40c1cec6d0b0c0d1178950418855"
    r = requests.post(f"http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&appid={appid}")
    data = json.loads(r.text)
    #temp = data['temp']
    return data


app = Flask(__name__)
@app.route("/<cityy>/")
def home(cityy):
    d = get_data(cityy)
    icon = d['weather'][0]['icon']
    t = d['main']['temp']
    icon_URL = f"http://openweathermap.org/img/wn/{icon}@2x.png"
    return render_template("index.html", c = cityy, t = t, icon_URL = icon_URL)

if "__main__" == __name__:
    app.run(debug=True)

