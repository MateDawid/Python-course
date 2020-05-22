import pylab
x = range(-5,6)
y = []
for i in x:
    score = 2*i+1
    y.append(score)
pylab.plot(x,y,color='purple')
pylab.grid(True)
pylab.title("Wykres funkcji y=2x+1")
pylab.show()
