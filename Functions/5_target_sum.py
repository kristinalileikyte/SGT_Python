# A function that takes a list of integers and a target sum as parameters and returns a list of two integers from the original list that add up to the target sum.

integers = [1,5,3,8,-2,99,30,4,78,6,54,-24,32]

target_sum = 97

def targeting_sum(list, target):
    count = 0
    for integer in list:
        count += 1
        for i in range(count,len(list)):
            if integer + list[i] == target:
                return [integer,list[i]]
            else:
                continue


print(targeting_sum(integers,target_sum))