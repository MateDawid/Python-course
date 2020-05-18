word = input("Podaj wyraz: ")
word2 = ""
for i in word:
    if i == "*":
        word2 += ""
    else: 
        word2 += i
print (word2)