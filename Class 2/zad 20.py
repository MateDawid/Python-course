word = input("Podaj wyraz: ")
lenght = len(word)
for i in range(lenght-1,-1,-1):
    print(word[i],end="")
