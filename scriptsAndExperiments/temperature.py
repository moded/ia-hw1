import numpy as np
from matplotlib import pyplot as plt
import functools
import numpy.matlib

X = np.array([400,900,390,1000,550]).reshape(5,1)
T = np.arange(0.01,5,0.0499).reshape(1,100)

alpha = min(X)
X_div_alpha =  np.matlib.repmat( X / alpha, 1, T.size )
p = np.power(X_div_alpha, -1 / T)
denom = np.sum(p, 0).reshape(1,100)
p = p / denom
# Xs = functools.reduce(lambda x,y: x+y,(X/alpha)**(-1/T))
# Pr = ((X/alpha)**((-1/T)))/Xs
plt.plot(np.transpose(p))
plt.show()
plt.title("Probability as a function of Temprature")

# TODO : Write the code as explained in the instructions
#raise NotImplementedError
