from datetime import datetime, date, timedelta, timezone


#getting the current date and time
current_time = datetime.now()

print("Current date and time:", current_time)


#creating a specific date
birthday = date(2008, 5, 15)

print("Birthday:", birthday)
print("Year:", birthday.year)
print("Month:", birthday.month)
print("Day:", birthday.day)


#formatting a date
current_time = datetime.now()

formatted_date = current_time.strftime("%d/%m/%Y")

print("Formatted date:", formatted_date)


#calculating the difference between two dates
first_date = date(2026, 9, 1)
second_date = date(2026, 9, 27)

difference = second_date - first_date

print("Number of days:", difference.days)


#adding days to a date
today = date.today()

future_date = today + timedelta(days=10)

print("Today:", today)
print("Date after 10 days:", future_date)


#working with UTC timezone
utc_time = datetime.now(timezone.utc)

print("UTC time:", utc_time)