# A function that takes a string as a parameter and returns True if the string is a palindrome and False otherwise.

answer = input("Write a palindrome: ")

def is_palindrome(palindrome):
    list = []
    for symbol in palindrome:
        list.append(symbol)

    reversed_list = list[:]
    reversed_list.reverse()

    if list == reversed_list:
        return True
    else:
        return False
    
    
print(is_palindrome(answer))