def solution(A):
    sum = 0
    for i in A:
        if i%2==0:
            sum += i
    return sum

#test
print(solution([-6,-91,1011,-100,84,-22,0,1,473]))