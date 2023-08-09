"""
    create env variables and store auth_key and account_sids for security purposes, while sharing the code.
"""

import requests
from twilio.rest import Client

api = "0e3f00f0fc92bf7d8fcfb621d2f2f6ab"
end_point = "https://api.openweathermap.org/data/2.5/onecall"

# twilio account_sid and authkey
account_sid = ""
auth_key = ""
from_number = "1234567890"
to_number = "0987654321"

weather_parameters = {
    "lat": 12.971599,
    "lon": 77.594566,
    "appid": api,
    "exclude": "minutely,current,daily"
}

# response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
# response = requests.get(url="https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=0e3f00f0fc92bf7d8fcfb621d2f2f6ab")

response = requests.get(url=end_point, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain = True

if will_rain:
    # we send sms here
    client = Client(account_sid, auth_key)
    message = client.messages.create(
        body="It's going to rain today.\nRemember to bring an Umberla!",
        from_=from_number,
        to=to_number,
    )

print(message.status)

