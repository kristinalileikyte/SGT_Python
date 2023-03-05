year = int(input("Please enter a year: "))

leap_year = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

print(f"Leap year: {leap_year}")