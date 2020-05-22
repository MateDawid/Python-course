#dictionary = {"jabłko":"apple","gruszka":"pear"}
#word = input("Podaj słowo: ")
#if word in dictionary:
#    print("Tłumaczenie:",dictionary[word])
polish_words = ['mama','tata','witam','dom']
english_words = ['mum','dad','hello','house']

polish_word = input('Podaj słowo po polsku: ')
try:
    index = polish_words.index(polish_word)
    print("Słowo po angielsku to:",english_words[index])
    pass
except:
    print("Nie znaleziono słowa w słowniku.")

