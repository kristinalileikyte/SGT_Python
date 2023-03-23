# A function that takes a tuple as a parameter and returns a new tuple that has the first and last elements swapped.

fullname = ('name','surname')

swap = lambda tuple : tuple[::-1]

print(swap(fullname))