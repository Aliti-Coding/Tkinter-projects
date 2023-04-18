from smtplib import SMTP
import datetime as dt
from random import choice

now = dt.datetime.now()

date = now.date()
day_of_week = now.weekday()

if day_of_week == 0:
        
    with open("quotes.txt", "r") as file:
        data = file.readlines()

    random_quote = choice(data)
    
    print(random_quote)
    my_email = "alitv1998you@gmail.com"
    password = ""

# #creating connection to email server
    with SMTP("smtp.gmail.com",  port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        subject = "Monday motivational quote!"
        body = random_quote

        connection.sendmail(
            from_addr=my_email, 
            to_addrs=[""], 
            msg=f"Subject: {subject}\n\n {body}")
