# A function that takes a set as a parameter and returns a new set that contains only the elements that are not divisible by 3.

integers = [1,5,3,8,-2,99,78,6,54,-24,32]

def not_divisible(ints):
    new_set = set()
    for int in ints:
        if int % 3 != 0:
            new_set.add(int)
    return new_set

print(not_divisible(integers))
