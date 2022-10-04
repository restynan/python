import datetime as dt
import os

import pandas
import random
import smtplib

MY_EMAIL = "birungimariam883@gmail.com"
PASSWORD = ""
PLACEHOLDER = "[NAME]"

# Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()

birth_day_data_frame = pandas.read_csv("birthdays.csv")
#print(birth_day_data_frame.to_dict(orient="records"))


bd_names_email = [{"name": row["name"], "email": row["email"]} for (index, row) in birth_day_data_frame.iterrows()
                   if row.month == today.month and row.day == today.day]
#  pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
#random_letter = random.choice(os.listdir())

with open(f'letter_templates/letter_{random.randint(1,3)}.txt', "r") as letter_file:
    letter = letter_file.read()
    for person in bd_names_email:
        new_letter = letter.replace(PLACEHOLDER, person["name"])
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=person["email"],
                                msg=f"subject:Happy Birthday\n\n{new_letter}"
                                )
