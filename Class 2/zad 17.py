import turtle
win = turtle.Screen() # pojawia się okno
square = turtle.Turtle() # tworzenie zmiennej, na której będzie rysowane
for i in range(4):
    square.forward(100) #100 pikseli prosto
    square.left(90) #obrót o 90 stopni
win.mainloop() #powoduje niezamykanie się okna