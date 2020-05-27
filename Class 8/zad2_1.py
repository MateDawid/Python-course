import math

def is_square(n):
    sqrt = math.sqrt(n)
    return (sqrt - int(sqrt) ==0)
print(is_square(128))
print(is_square(17))