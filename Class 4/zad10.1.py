n = int(input('Podaj liczb elementow\n'))
list = []
# how to get max in list in python
# odczyt danych do list
for i in range(1,n+1):
    number = int(input('Podaj liczbe '))
    list.append(number)
print(max(list))
print(sorted(list))
max = list[0] # na poczatku zaklady ze maxem jest element 0
# przechodzimy po wszystkich elementach
for value in list:
    # jakis element jest wiekszy to max staje sie ten element
    if value>max:
        max = value
print('Maksymalny element to ',max)