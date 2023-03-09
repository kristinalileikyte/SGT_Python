print("Let's do math!")

a = int(input("Number: "))

operator = input("Operator: ")
legit_operator = ("*","/","+","-","%")

while operator not in legit_operator:
    operator = input("Operation provided isn't valid, please, try again: ")

b = int(input("Number: "))

while operator == "/" :
    if b == 0:
        b = int(input("Zero division is not happening, please try other number: "))
    else:
        break

if operator == "*":
    print(a*b)
elif operator == "/":
    print(a/b)
elif operator == "+":
    print(a+b)
elif operator == "-":
    print(a-b)
else:
    print(a%b)

