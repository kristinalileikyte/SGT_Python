# A function that takes a list of integers as a parameter and returns the product of all the integers in the list.

integers = [1,5,3,8,-2,99,30,4,78,6,54,-24,32]

def product(list):
    product = 1
    for integer in list:
        product *= integer
    return product


print(product(integers))