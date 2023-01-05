from flask import Flask
import requests
from redis import Redis
import random
import os

app = Flask(__name__)
region = os.environ['REGION']
redis = Redis(host='redis', port=6379)

cur_EU = ["EUR", "CHF", "GBP"]        
cur_NONEU = ["AUD", "CAD", "USD", "JPY"]
              
api_url = "http://api.nbp.pl/api/exchangerates/rates/a/{}/"

def nbp_call(currency):
    response = requests.get(api_url.format(currency))

    return response.json()
    
@app.get("/")
def home():
    redis.incr('hits')
    counter = str(redis.get('hits'), 'utf-8')

    if region != "EU":
        value = nbp_call(random.choice(cur_NONEU))
    else:
        value = nbp_call(random.choice(cur_EU))

    
    return f"""<div align='center'><h3>1 {value['code']} = {value['rates'][0]['mid']} PLN
    <br><br>
    This page has been viewed {counter} times</h3></div>"""
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
