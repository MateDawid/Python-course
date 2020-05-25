def palindrom(word):
    return word[::-1] == word

x = input("Podaj wyraz: ")
print(palindrom(x))