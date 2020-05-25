def array_sum(array):
    return array[0]+array[1]
array = []
try:
    x = int(input("Podaj pierwszy element listy: "))
    y = int(input("Podaj drugi element listy: "))
    array.append(x)
    array.append(y)
    print(array)
    print(array_sum(array))
except:
    print ("Podano nieprawidłowe dane")