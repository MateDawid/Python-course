def solution(A):
    array = set(A)
    if max(array) < 0:
        return 1
    for i in range (1,max(array)+2):
        if i not in array:
            return i

print(solution([1,2,3,6]))