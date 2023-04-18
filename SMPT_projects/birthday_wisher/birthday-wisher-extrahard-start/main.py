import csv
import datetime as dt
import smtplib
import os 
from random import choice



#Create\Update the birthdays.csv

birthday_list = [
    {'name': 'alitv','email': 'fehmmialiti@yahoo.com','year': '1978', 'month': 4,'day': 17},
    {'name': 'alitv','email': 'alitiv1998you@gmail.com','year': '1978', 'month': 4,'day': 17}
]

class BuildingFile:
    """ This class creates a csv file if not exists
    if csv file exist you can append data to csv file
    
    it is optional to add 1 member to the csv file or
    to add a list of more members 
    """
    def __init__(self, filename:str, name:str=None, email:str=None, year:int=None, month:int=None, day:int=None, birthdays=None):
        self.filename = filename
        self.name = name
        self.email = email
        self.year = year
        self.month = month
        self.day = day
        self.birthdays = birthdays
    
    def building_file(self):
        try:        
            with open(self.filename, "r", newline='') as datafile:
                data = csv.DictReader(datafile, delimiter=',') 
                existing_emails = [rows['email'] for rows in data]
        except:
            with open(self.filename, "w", newline='') as datafile:
                header = ['name', 'email', 'year', 'month', 'day']
                data = csv.DictWriter(datafile, delimiter=',', fieldnames=header)
                data.writeheader()
                
        else:
            with open(self.filename, "a", newline='') as datafile:
                header = ['name', 'email', 'year', 'month', 'day']
                write_line = csv.DictWriter(datafile, delimiter=',', fieldnames=header)
            
                #check if email exist in csv file if not append birthday list
                if self.birthdays != None:
                    for rows in self.birthdays:
                        if rows['email'] not in existing_emails:
                            write_line.writerow(rows)

                #if there is name input we add if not we dont add
                if self.name != None:
                    if self.email not in existing_emails:
                        birthday_oneline = {'name': self.name, 'email': self.email, 'year': self.year, 'month': self.month, 'day': self.day}
                        write_line.writerow(birthday_oneline)

                
    def __repr__(self) -> str:
        return f"filename: {self.filename}, birthday: {self.birthdays}"

filepath = r"SMPT_projects\birthday_wisher\birthday-wisher-extrahard-start\birthdays.csv"
file = BuildingFile(filename=filepath)
# building the file
file.building_file()


#Check if today matches a birthday in the birthdays.csv if yes return a dictionary with email and text
def letter():
    date_now = dt.datetime.now()
    year = date_now.year
    month = date_now.month
    day = date_now.day

    with open(filepath, "r", newline='') as datafile:
        data = csv.DictReader(datafile, delimiter=',')

        letters_to_send = {}

        for row in data:
            if month == int(row['month']) and day == int(row['day']):

                #select a random letter            
                letter_files = os.listdir(r'C:\Users\fehmm\OneDrive\Skrivebord\python\100_days_python\projects_github\Tkinter-projects\SMPT_projects\birthday_wisher\birthday-wisher-extrahard-start\letter_templates')
                random_letter = choice(letter_files)

                #open the letter
                with open(fr"C:\Users\fehmm\OneDrive\Skrivebord\python\100_days_python\projects_github\Tkinter-projects\SMPT_projects\birthday_wisher\birthday-wisher-extrahard-start\letter_templates\{random_letter}", "r") as letterfile:
                    letter = letterfile.read()
                    personalized_letter = letter.replace('[NAME]', row['name'])
                    print(row['email'])
                    letters_to_send[row['email']] = personalized_letter
                    
        return letters_to_send


class SendMail():
    def __init__(self, letter_dict:dict) -> None:
        self.letter_dict = letter_dict

    def mail_sender(self, from_adr:str):
        with smtplib.SMTP("smtp.gmail.com") as server:
            # letter_dict = letter() # dictionary with letters to send
            from_adr = "alitv1998you@gmail.com"
            password = ""
            server.starttls()
            server.login(from_adr, password)
            
            for key, value in self.letter_dict.items():
                server.sendmail(
                    from_addr=from_adr,
                    to_addrs=key,
                    msg=f"Subject: Happy Birthday!\n\n {value}"

                )



#sending mail
sendmail = SendMail(letter())
sendmail.mail_sender("alitv1998you@gmail.com")