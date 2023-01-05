from flask import Flask
from redis import Redis
import requests
import random


app = Flask(__name__)
redis = Redis(host='redis', port=6379)

currencies = ["AUD", "THB", "BRL", "BGN", "CAD", "CLP", "CZK",
              "DKK", "EUR", "HUF", "HKD", "UAH", "ISK", "INR",
              "HRK", "MYR", "MXN", "ILS", "NZD", "NOK", "PHP",
              "GBP", "ZAR", "RON", "IDR", "SGD", "SEK", "CHF",
              "TRY", "USD", "KRW", "JPY", "CNY", "XDR"]
              
api_url = "http://api.nbp.pl/api/exchangerates/rates/a/{}/"

def nbp_call(currency):
    response = requests.get(api_url.format(currency))

    return response.json()
    
    
@app.get("/")
def home():
    redis.incr('hits')
    counter = str(redis.get('hits'), 'utf-8')
    value = nbp_call(random.choice(currencies))

    return f"""<div align='center'><h3>1 {value['code']} = {value['rates'][0]['mid']} PLN</h3></div>
    <br><br>
    This page has been viewed {counter} times"""
    

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
