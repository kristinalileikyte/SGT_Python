day, month, year = input("Please enter the date (day month year): ").split()

day = int(day)
month = int(month)
year = int(year)
leap_year = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

valid_year = (year > 0) and (year < 10000)
valid_month = (month > 0) and (month <= 12)
valid_day = (
    day > 0 
    and ((
        (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day <= 31) 
        or 
        (leap_year == False and month == 2 and day <= 28) 
        or 
        (leap_year and month == 2 and day <= 29) 
        or 
        ((month == 4 or month == 6 or month == 9 or month == 11) and day <= 30)
    ))

valid_date = valid_day and valid_month and valid_year

print(f"Date valid: {valid_date}")