for i in range(5,101):
    score = 0
    for j in range(1,i+1):
        if i%j==0:
            score += 1
    if score == 4:
        print(i)