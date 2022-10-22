import requests
import datetime as dt
import time
import smtplib

# if the ISS is close to my current location
# and its currently dark
# send an email and tells me to look  up
# https://www.latlong.net/Show-Latitude-Longitude.html
MY_LATITUDE = 44.314842
MY_LONGITUDE = -85.602364

MY_EMAIL = "birungimariam883@gmail.com"
PASSWORD = ""


def is_iss_over_head():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    print(f'iss status code: {response.status_code}')
    response.raise_for_status()
    response_data = response.json()
    print(f'iss api response data : {response_data}')
    iss_latitude = float(response_data["iss_position"]["latitude"])
    iss_longitude = float(response_data["iss_position"]["longitude"])
    iss_position = (iss_latitude, iss_longitude)
    print(f"iss_position: {iss_position}")

    if MY_LATITUDE - 5 <= iss_latitude <= MY_LATITUDE + 5 and MY_LONGITUDE - 5 <= iss_longitude <= MY_LONGITUDE + 5:
        print("iss is over head")
        return True
    return False


# https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400
def is_night_time():
    parameters = {
        "lat": MY_LATITUDE,
        "longitude": MY_LONGITUDE,
        "formatted": 0
    }
    response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_sun.raise_for_status()
    print(f'sunrise sunset api response: {response_sun.json()}')
    sun_rise_hour = int(response_sun.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    print(f'sunrise hour: {sun_rise_hour}')
    sun_set_hour = int(response_sun.json()["results"]["sunset"].split("T")[1].split(":")[0])
    print(f'sunset hour: {sun_set_hour}')
    current_hour = dt.datetime.now().hour
    print(f'current hour: {current_hour}')
    if current_hour >= sun_set_hour or current_hour <= sun_rise_hour:
        print("night time")
        return True
    return False


is_iss_over_head()
is_night_time()

while True:
    time.sleep(60)
    if is_night_time() and is_iss_over_head():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="lucyKatana355@yahoo.com",
                                msg="subject:Lookup \n\n The iss is above you in the sky"
                                )


# data types of variables of inputs and outputs

def police_check(age: int) -> str:
    if age > 18:
        return 90
    else:
        return "can't drive"


print(police_check(50))
