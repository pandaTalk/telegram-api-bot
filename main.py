import json
import requests
from bs4 import BeautifulSoup as bs

def request_USDT_BTC():
    r = requests.get('http://poloniex.com/public?command=returnTicker')
    parsedjson = json.loads(r.text)
    value = parsedjson["USDT_BTC"]["last"]
    return str(value)


def request_hsi():
    r = requests.get(
        'http://finance.now.com/api/getAfeQuote.php?item=allindex')
    parsedjson = json.loads(r.text)
    value = parsedjson["indexInfos"][0]["index"]
    return str(value)

def request_stock(quoteSymbol):
    r = requests.get(
        "http://www.aastocks.com/tc/stocks/quote/detail-quote.aspx?symbol=" + quoteSymbol,
        timeout=10)
    responseCookies = r.cookies
    responseCookies["AALTP"] = '1'
    r = requests.get(
        "http://www.aastocks.com/tc/stocks/quote/detail-quote.aspx?symbol=" + quoteSymbol,
        cookies=responseCookies)

    html_body = bs(r.text, 'html.parser')
    value = html_body.select_one("#labelLast > b > span").contents[1]
    return str(value)

def sendMessage(chat_id, message):
    payload = {"chat_id": chat_id, "text": message}
    requests.post(
        'https://api.telegram.org/bot394851849:AAGqhMqnurc6QwIz759hDwig8O-_Uu0ACYg/sendMessage',
        data=payload)

def main(event, context):
    input_json = json.loads(event["body"])
    if "message" in input_json:
        input_json = input_json["message"]
        if "chat" in input_json:
            chat_id = input_json["chat"]["id"]
            if "entities" in input_json:
                is_command = input_json["entities"][0]["type"] == "bot_command"
                if is_command:
                    command = input_json["text"]
                    offset = input_json["entities"][0]["offset"]
                    length = input_json["entities"][0]["length"]
                    message = ""
                    if "/getbtc" in command:
                        message = request_USDT_BTC()
                    elif  "/gethsi" in command:
                        message = request_hsi()
                    elif "/getall" in command:
                        message = "BTC: " + request_USDT_BTC()
                        message += "\nHSI: " + request_hsi()
                    elif "/getstock" in command:
                        qouteNumber = command[length:]
                        if qouteNumber:
                            message = "Stock " + qouteNumber + ": " + request_stock(qouteNumber)
                        else:
                            message = "Require Stock Symbol"


                    if message != "":
                        sendMessage(chat_id, message)

    res = {"statusCode": 200, "headers": {}}
    return res
