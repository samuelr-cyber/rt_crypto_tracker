# ./tracker.py

from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import Intervaltrigger
from pusher import Pusher
import requests, json, atexit, time, plotly, plotly.graph_objs as go

# Intialize these variables
# create flask app
app = Flask(__name__)

# configure pusher object
pusher = Pusher(
    app_id = 'app_id',
    key = 'key',
    secret = 'secret',
    cluster = 'cluster',
    ssl = True
)

# define variables for data retrieval
times = []
currencies = ["BTC","ETH","BNB","ADA","DOT","LTC"]
prices = {"BTC":[], "ETH":[], "BNB":[], "ADA":[], "DOT":[], "LTC":[]}

@app.route("/")
def index():
    return render_template("index.html")
