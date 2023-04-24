import requests

channels_url = "https://api.wazzup24.com/v2/channels"

headers = {
    "Authorization": "", #authorization token here
    "Content-Type": "application/json",
}

channel_id = requests.get(channels_url, headers = headers).json()[0]['channelId']

print(channel_id)

