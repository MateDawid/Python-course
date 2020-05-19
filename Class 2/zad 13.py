import random
number = random.randrange(1,10)
answer = []
while  answer != number:
    answer = int(input("Podaj odpowiedź: "))
    if answer > number:
        print("Za dużo.")
    elif answer < number:
        print("Za mało.")
print("Gratulacje")