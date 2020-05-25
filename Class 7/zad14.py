import zad11_1 as f
max = 0
for i in range(2,10001):
    if f.number_of_divisors(i)>f.number_of_divisors(max):
        max = i
print(max)
print(f.number_of_divisors(max))