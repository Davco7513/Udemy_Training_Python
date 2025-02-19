import datetime as dt
import random
import smtplib

'''my_email = "colemandavid2000@gmail.com"
password = "vtno bgvy izhu okhf"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="colemandpro@gmail.com", msg="Hello")
    connection.close()'''

MY_EMAIL = "colemandavid2000@gmail.com"
MY_PASSWORD = "vtno bgvy izhu okhf"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Monday Motivation\n\n{quote}")
