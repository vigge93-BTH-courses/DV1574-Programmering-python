import matplotlib.pyplot as pl
import numpy

x = numpy.linspace(0, 20, 100) # Creates an array with 100 elements evenly distibuted between 0 and 20
pl.plot(x, numpy.sin(x))
pl.show()