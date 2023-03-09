integer = int(input("Lets's check if your integer is a prime number: "))

prime = True

for i in range(2,integer):
    if integer % i == 0:
        print("Sorry, it's a composite number.")
        prime = False
        break
        
if prime:
    print("Congratulations, it's a Prime!")
