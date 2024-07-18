#Funçao do 1 grau
#y = ax+b
import numpy as np
import matplotlib.pyplot as plt
a = 2
b = 0
x = np.linspace(-10,10,20)
y=a*x+b
plt.plot(x,y,".")