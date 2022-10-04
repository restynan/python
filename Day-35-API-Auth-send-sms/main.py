# rain alert if its going to rain  btn 7:am - 7pm , sent   sms at 7am before i head out for the day.
# https://api.openweathermap.org/data/2.5/onecall?lat=44.314842&lon=-85.602364&exclude=current,minutely,daily&appid=69f04e4613056b159c2761a9d9e664d2
#https://www.ventusky.com/
#https://www.latlong.net/
#https://openweathermap.org/api/one-call-3#example
#https://openweathermap.org/weather-conditions

import requests
import os
from twilio.rest import Client



weather_params = {
    'lat': 40.712776,
    'lon': -74.005974,
    'appid': API_KEY,
    'exclude': "current,minutely, daily"
}
response = requests.get(OWE_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    weather_code = hour_data["weather"][0]["id"]
    if will_rain:
        break
    if int(weather_code) < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="it's going to rain today. Remember to bring an umbrella ☔️",
            from_='+13856854943',
            to='+16418191250'
        )
        print("raining")
        print(message.status)
        print(message.sid)
        will_rain = True






