def solution(A):
    summary = 0
    for i in A:
        if i%2 == 0:
            summary+=i
    return summary
        
#test

print (solution([-6,-91,1011,-100,84,-22,0,1,473]))

