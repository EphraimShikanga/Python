import datetime

year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))
birthday = datetime.date(year, month, day)
today = datetime.date.today()
age = today - birthday
years = age.days // 365
months = (age.days // 30)
days = age.days
print(f"You are {years} years old.")
print(f"You are {months} months old.")
print(f"You are {days} days old.")
