a, b = input("Please enter two integers: ").split()

a = int(a)
b = int(b)

even = (a % 2 == 0) and (b % 2 == 0)

print(f"Both numbers are even: {even}")

one_even = (a % 2 == 0) or (b % 2 == 0)

print(f"At least one number is even: {one_even}")