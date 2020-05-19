number = int(input("Podaj liczbę: "))
value_1 = 1
value_2 = 1
final_sum = 0
for i in range(3, number+1):
    final_sum = value_2
    value_2 = value_1 + value_2
    value_1 = final_sum
print(value_2)
     