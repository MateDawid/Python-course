def solution(A):
    s = set(A)
    for i in range(1,len(A)+2):
        if not i in s:
            return i
