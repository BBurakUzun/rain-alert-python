import requests
import os
from twilio.rest import Client

api_key = os.environ["API_KEY"]
account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]
my_phone = os.environ["PHONE"]

response = requests.get(
    url=f"https://api.openweathermap.org/data/2.8/onecall?lat=40.96&lon=29.23&exclude=current,minutely,daily&appid={api_key}")

print(response.status_code)
response.raise_for_status()

weather_data = response.json()
print(weather_data["hourly"])

will_rain = False
weather_conditions = []

for hour_data in weather_data["hourly"][:12]:
    hava_kodu = hour_data["weather"][0]["id"]
    if int(hava_kodu) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(body="🔥🔥🔥🔥", from_="+12512782401", to=my_phone
    )

    print(message.sid)
