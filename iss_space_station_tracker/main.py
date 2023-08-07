import requests
import datetime as dt
import smtplib
import time
# ISS space station api documentaion
# http://open-notify.org/Open-Notify-API/ISS-Location-Now/

# sunrise and sunset times api
# "https://api.sunrise-sunset.org/json"

my_email = "luckytest140@gmail.com"
password = "password@1234"

MY_LAT = 18.279432
MY_LONG = 77.602072


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LONG - 5 <= longitude <= MY_LONG + 5:
        return True
    else:
        return False


def night_time():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now = dt.datetime.now().hour

    if now >= sunset or now <= sunrise:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_iss_overhead() and night_time():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="lakshmanlucky821@gmail.com",
                                msg="Subject: Look Up \n\n ISS is above you in the sky!")


