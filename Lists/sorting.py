# Heterogenous list:
list = ["apple","Almond",2,"Kiwi","+","banana",5,"coffee",-1,"Pancakes"]


# Splits main list in two new lists (one for integers and other one for strings):
numList = [] 
strList = []

for i in range(len(list)):
    if isinstance(list[i], int):
        numList.append(list[i])
    else:
        strList.append(list[i])

newNumList = numList[:]
newStrList = strList[:]


# Sorts integer list in ascending order:
for i in range(len(numList)):
    index = -1
    for j in range(len(numList)):
        if numList[i] >= numList[j]:
            index += 1
    newNumList[index] = numList[i]


# Sorts string list in ascending order (first symbols, than strings with uppercases and lastly, lowercase strings):
for i in range(len(strList)):  
    index = -1
    for j in range(len(strList)):
        if strList[i] >= strList[j]:
            index += 1
    newStrList[index] = strList[i]


# Joins both lists:
output = newNumList + newStrList


# Prints output:
print(f"Here is heterogenous list in given order: integers, symbols, uppercase strings, lowercase strings: \n{output}")