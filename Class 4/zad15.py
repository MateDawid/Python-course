import pylab
x = range(-10,16)
y = []
for i in x:
    score = 3*i+15
    y.append(score)
pylab.plot(x,y,color="black")
pylab.grid(True)
pylab.title("Wykres funkcji y = 3x + 15")
pylab.show()