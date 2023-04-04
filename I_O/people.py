# Write a Python program that reads a JSON file containing a list of dictionaries, sorts the list by a specific key, and writes the sorted list back to the file.

import json


with open("people.json","r") as file:
    persons = json.load(file)["people"]
    
persons.sort(key=lambda x: x["firstName"])   

with open("people.json","w") as file:
    json.dump({"people":persons},file)
    


    

