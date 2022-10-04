import smtplib
import random
import datetime as dt

MY_EMAIL = "birungimariam883@gmail.com"
PASSWORD = ""

now = dt.datetime.now()
if now.weekday() == 1:
    with open("quotes.txt", "r") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="lucyKatana355@yahoo.com",
                            msg=f"subject:Today's Motivation\n\n{quote}"
                            )
'''
import datetime as dt

now = dt.datetime.now()
print(now)
# year
year = now.year
if year == 2022:
    print("wear a mask")

day_of_the_week = now.weekday()
# note monday - 0
print(day_of_the_week)

# create a datetime object
date_of_birth = dt.datetime(year=1995, month=5, day=15)
print(date_of_birth)
'''
