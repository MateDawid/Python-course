def fiveLetter(array):
    results = []
    for i in array:
        if len(i) == 5:
            results.append(i)
    return results

#test

print(fiveLetter(['dawcio','jakub','kalcia']))