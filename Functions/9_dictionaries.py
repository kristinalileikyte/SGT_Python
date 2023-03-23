# A function that takes a list of dictionaries as a parameter and returns a new dictionary that contains the sum of the values for each key in the original dictionaries.

precipitation =  [
    { 'Country': 'Lithuania', 'January': 51, 'February': 38, 'March': 42, 'April': 36, 'May':54, 'June': 75, 'July': 78, 'August': 77, 'September': 65, 'October': 66, 'November': 58, 'December': 55},
    { 'Country': 'Latvia', 'January': 50, 'February': 35, 'March': 35, 'April': 30, 'May':35, 'June': 45, 'July': 55, 'August': 70, 'September': 65, 'October': 75, 'November': 65, 'December': 60},
    { 'Country': 'Estonia', 'January': 55, 'February': 35, 'March': 35, 'April': 35, 'May':40, 'June': 65, 'July': 80, 'August': 85, 'September': 60, 'October': 75, 'November': 65, 'December': 60}
    ]

def count_sum(list):
    for country in list:
        mm = 0
        for value in country:
            if isinstance(country[value],int):
                mm += country[value]       
        print(f"{country['Country']}: {mm} milimeters.")   


count_sum(precipitation)