from datetime import datetime

current_time = datetime.now()
print(current_time)

mybirthday = datetime(1999,11,20,7,30,11,23)
print(mybirthday)
print(mybirthday.year)
print(mybirthday.month)
print(mybirthday.day)
print(mybirthday.hour)
print(mybirthday.minute)
print(mybirthday.second)
print(mybirthday.microsecond)
print(mybirthday.weekday())

print(datetime(2020,1,1) - datetime(2018,1,1))
print(datetime.now() - datetime(1999,1,20))

parsed_date = datetime.strptime("Jul 13, 2019","%b %d, %Y")
print(parsed_date)
print(parsed_date.year)
print(parsed_date.month)
print(parsed_date.day)

date_string = datetime.strftime(datetime.now(), "%b %d, %Y")
print(date_string)
