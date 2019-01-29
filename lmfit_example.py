from lmfit import Model
import numpy
from matplotlib import pyplot as plt


#  define the Model's function
def decay(t, tau, N):
    return N*numpy.exp(-t/tau)

#  make some noisy data
t = numpy.linspace(0, 30)
data = decay(t, 3, 30) + numpy.random.random(50) * 3

#  create a Model object
decay_model = Model(decay)

#  fit the model to data
result = decay_model.fit(data, tau = 5, N = 3, t = t)

# plot the results
plt.plot(t, data, '.')
plt.plot(t, result.eval())
plt.grid()
plt.show()