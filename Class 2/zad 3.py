word = input("Podaj wyraz: ")
reverse = word[::-1]
if word == reverse:
    print("Palindrom")
else:
    print("Różne wyrażenia")