import json
import requests
import datetime
import os

SITE = os.environ['telegram_key']
CHAT_ID = os.environ['chat_id']

def lambda_handler(event, context):
    r = requests.get('http://poloniex.com/public?command=returnTicker')
    parsedjson = json.loads(r.text)
    utc_now = datetime.datetime.utcnow()
    local_time_delta = datetime.timedelta(hours=8)
    local_now = now + local_time_delta
    message = "Time: " + local_now.strftime() + "\n"
    message += "Last Price: " + parsedjson["USDT_BTC"]["last"]
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(
        'https://api.telegram.org/bot'+SITE+'/sendMessage',
        data=payload)
