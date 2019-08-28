import matplotlib.pyplot as pl
import numpy

# Creates an array with 100 elements evenly distibuted between 0 and 20
x = numpy.linspace(0, 20, 100)

pl.plot(x, numpy.sin(x))  # x, f(x)
pl.show()
