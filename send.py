import requests
import json
import time

text = "Тестовое сообщение"

headers = {
    "Authorization": "", #authorization token here
    "Content-Type": "application/json",
}

data = {
    "user": {
        "id": "9330-1485",
        "name": "Voltman",
    },
    "scope": "global",
    "channelId": "16317bf2-08b0-48fe-876d-b7f57bd9e9e8",
    "chatType": "whatsapp",
    "chatId": "", #phone number
    "text": text,
}

print(json.dumps(data, separators = (',', ':')))

send_url = "https://api.wazzup24.com/v2/send_message"
for i in range(3):
    r = requests.post(send_url, headers = headers, data = json.dumps(data, separators = (',', ':')))

print(r.json())