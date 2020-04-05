import json
import urllib.request, urllib.parse
from flask import Flask, render_template, request

app = Flask(__name__, template_folder = 'template')


@app.route('/', methods = ['GET', 'POST'])
def home():
    try:
        data = request.args.get('city')
        if data != None :
            data = get_weather(data)
        else:
            data = get_weather('Hà Nội')
        return render_template('home.html', data =data)
    except:
        return render_template('home.html', data = {})

def get_weather(query):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=9c86e651ab368c7b4df0fd4226335436"
    query = urllib.parse.quote(query)
    url = api_url.format(query)
    open_url =urllib.request.urlopen(url)
    data = json.load(open_url)

    weather = None
    if data.get('weather'):
        weather ={
            'description': data['weather'][0]['description'],
            'temperature': round(data['main']['temp'] -273,2),
            'city': data['name']
        }

    return weather

if __name__ ==  '__main__':
    app.run(debug = True)
