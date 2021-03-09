# ./.py

from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from pusher import Pusher
import requests, json, atexit, time, plotly, plotly.graph_objs as go

# Intialize these variables
# create flask app
app = Flask(__name__)

# configure pusher object
pusher = Pusher(
    app_id = '1169298',
    key = '233085aa2d53713dbbf7',
    secret = '61d9f1fae437c0a92e21',
    cluster = 'us2',
    ssl = True
)

# define variables for data retrieval
times = []
currencies = ["BTC"]
prices = {"BTC":[]}

@app.route("/")
def index():
    return render_template("index.html")
    # render_template is a function to serve index.html from ./templates from the folder in the index route

#Data retrieval function

def retrieve_data():
    #create dictionary to save current prices
    current_prices = {}
    for currency in currencies:
        current_prices[currency] = []
    #append new item to list of times
    times.append(time.strftime('%H:%M:%S'))
    #Make requests to the API and get the response as an object
    api_url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD,EUR".format(",".join(currencies))
    response = json.loads(requests.get(api_url).content)
    #append new price to list of prices for graph and set currrent prices for bar chart
    for currency in currencies:
        price = response[currency]['USD']
        current_prices[currency] = price
        prices[currency].append(price)

    #create an array of traces for graph data
    graph_data = [
        go.Scatter(
            x = times,
            y=prices.get(currency),
            name = "{} Prices".format(currency)
            )
        for currency in currencies
    ]

    bar_data = [
        go.Bar(
        x = currencies,
        y = list(current_prices.values())
        )
    ]

    data = {
        'graph' : json.dumps(list(graph_data), cls=plotly.utils.PlotlyJSONEncoder),
        'bar' : json.dumps(list(bar_data), cls=plotly.utils.PlotlyJSONEncoder)
    }

    # trigger event
    pusher.trigger("crypto","data-updated",data)

# The following code registers the job and runs our retrieve data function ever 10 seconds

#Create schedule for recieving prices
scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func = retrieve_data,
    trigger = IntervalTrigger(seconds=10),
    id = 'prices_retrieval_job',
    name = 'Retrieve prices every 10 seconds',
    replace_exisitng=True
)
# Shut down the scheduler when app is off
atexit.register(lambda:scheduler.shutdown())

#Run Flask App in debug mode
app.run(debug=True, use_reloader=False)
