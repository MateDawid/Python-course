def makeMiddle(array):
    if len(array)%2 == 1:
        return "Niewłaściwa wielkość tablicy."
    else:
        return [array[len(array)//2-1],array[len(array)//2]]

#test

print (makeMiddle([1,2,3,4]))
print (makeMiddle([1,2,3]))