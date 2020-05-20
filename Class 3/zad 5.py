word = input("Podaj wyraz: ")
lenght = len(word)
for i in range(lenght):
    print(word[i],end = " ")
for i,value in enumerate(word):
    print(value,end = " ")