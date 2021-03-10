# Real Time Crypto Currency Price Tracker
This is a real time cryptocurrency tracker built in Python. It has a list of several cryptocurrencies that the program will give real time price updates at set intervals of time. This program uses Pusher to receive updates and Plotly to visualize them. This project could be useful in the future for potentially tracking the long term growth of cryptocurrencies or create cryptocurrency trading bots.  

## Installation (Windows)
There are several dependencies to install before using this this tool. To run locally:
- Clone this repository
- Create a virtual environment in the project folder by entering the command in the folder's terminal:  
    - ``venv\Scripts\activate``
- Then install the dependencies:
    - ``pip install flask``
    - ``pip install requests``
    - ``pip install pusher``
    - ``pip install plotly``
- After this step there are some changes that need to be made to the code. To run this locally from your machine you must input new values in the ``Pusher()`` method of ``tracker.py``. To get these values you must setup a Pusher account, create an app for your tracker in channels, and finally get the app keys and plug them into the ``Pusher()`` method.
- The final step is to run the program using the command:
    - ``python tracker.py``
- Then go to the website address to make sure it's tracking.

## Built With

* [Pusher](https://pusher.com/) - APIs to enable devs building realtime features
* [Flask](http://flask.pocoo.org/) - Python web framework
* [Plotly](https://plot.ly/) - Data visualization tool
