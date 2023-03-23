# A function that takes a string as a parameter and returns the number of vowels (aeiou) in the string.

string = input("Write something for me: ")
vowels = "aeiou"

def vowels_count(str):
    count = 0
    for symbol in str:
        if symbol in vowels:
            count += 1
    return count

print(f"{vowels_count(string)} vowel(s) in your string!")
