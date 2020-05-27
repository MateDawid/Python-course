def frequency(array):
    result = array[0]
    for i in range(len(array)):
        if array.count(array[i])>array.count(result):
            result = array[i]
    return result
 
 #test

print(frequency([1,2,2,2,3]))
print(frequency(['a','a','b','c','d','d','d']))