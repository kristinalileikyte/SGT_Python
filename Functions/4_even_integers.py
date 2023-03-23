#  A function that takes a list of integers as a parameter and returns a list of only the even integers in the original list.

integers = [1,5,3,8,-2,99,78,6,54,-24,32]

def even(list)->list:
    new_list = []

    for i in range(0,len(list)):
        if list[i] % 2 == 0 :
            new_list.append(list[i])        
    return new_list


print(even(integers))
