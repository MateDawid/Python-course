file = open(r'\Users\Dawid\Desktop\Python\Akademia Kodu\11.05.2020\zad18.txt','r')
words = file.read()
dict = { }
for letter in words:
    if letter.isalpha():
        if letter in dict:
            dict[letter] = dict[letter]+1
        else:
            dict[letter] = 1
for letter in dict:
    print(letter,dict[letter])
