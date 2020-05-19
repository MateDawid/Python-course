secret_password = "Polska"
password = input("Podaj hasło:\n ")
while password != secret_password:
    password = input("Podaj poprawne hasło:\n")
print("Podano poprawne hasło. Gratulacje!")