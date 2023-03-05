age, license = input("Please enter your age and if you have your driver license (y/n): ").split()

ability = (int(age) >= 18) and license == "y"

print(f"You are able to drive: {ability}")