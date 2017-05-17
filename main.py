import requests
import json


def request_USDT_BTC():
    r = requests.get('http://poloniex.com/public?command=returnTicker')
    parsedjson = json.loads(r.text)
    value = parsedjson["USDT_BTC"]["last"]
    return value


def request_hsi():
    r = requests.get(
        'http://finance.now.com/api/getAfeQuote.php?item=allindex')
    parsedjson = json.loads(r.text)
    value = parsedjson["indexInfos"][0]["index"]
    return value

def sendMessage(chat_id, message):
    payload = {"chat_id": chat_id, "text": message}
    requests.post(
        'https://api.telegram.org/bot394851849:AAGqhMqnurc6QwIz759hDwig8O-_Uu0ACYg/sendMessage',
        data=payload)

def main(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    input_json = json.loads(event["body"])
    if "message" in input_json:
        input_json = input_json["message"]
        if "chat" in input_json:
            chat_id = input_json["chat"]["id"]
            if "entities" in input_json:
                is_command = input_json["entities"][0]["type"] == "bot_command"
                if is_command:
                    command = input_json["text"]
                    message = ""
                    if "/getbtc" in command:
                        message = request_USDT_BTC()
                    elif  "/gethsi" in command:
                        message = request_hsi()
                    elif "/getall" in command:
                        message = "BTC: " + request_USDT_BTC() + " HSI: " + request_hsi()

                    if message != "":
                        sendMessage(chat_id, message)

    returnvalue = ""
    res = {"statusCode": 200, "headers": {}, "body": event["body"]}
    return res