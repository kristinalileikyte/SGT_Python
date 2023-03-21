text = input("Please write a text: ").lower()
letter = input("Please give me a letter which you want to check: ").lower()

print(f"{text.count(letter)} occurence(s) of the letter {letter}.\n")

print("Occurence of the each character: ")

list = []
for i in range(len(text)):   
    if text[i] not in list:
        print(f"{text[i]}: {text.count(text[i])}")

    list.append(text[i])
