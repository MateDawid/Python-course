import pylab
x = range(5,16)
y = []
for i in x:
    score = i*i
    y.append(score)
pylab.plot(x,y)
pylab.show()