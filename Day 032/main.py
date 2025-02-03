import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "test@email.com"
MY_PASSWORD = ""

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple] # accessing the data_row
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
        contents = letter.read()
        stripped_name = birthday_person["name"].strip()
        personalised_message = contents.replace("[NAME]", stripped_name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{personalised_message}")
