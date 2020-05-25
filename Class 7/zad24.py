def maximum(array):
    result = array[0]
    for i in array:
        if i>result:
            result = i
    return result

#test

print(maximum([2,3,6,1,2]))