word = input("Podaj wyraz: ")
left = 0
right = len(word)-1
is_palindrom = True
while left<right:
    if word[left] != word[right]:
        is_palindrom = False
        break
    left+=1
    right-=1
if is_palindrom == True:
    print("Podane słowo to palindrom.")
else:
    print("Podane słowo nie jest palindromem.")