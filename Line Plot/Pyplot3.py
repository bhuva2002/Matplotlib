# importing package
import matplotlib.pyplot as plt
import numpy as np
  
#plt.rcParams["figure.figsize"] = [7.50, 3.50]
#plt.rcParams["figure.autolayout"] = True
#x = np.linspace(-10, 10, 100)

# create data
x=np.arange(0,15,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
  
#plt.fill_between(x, y1, 25000000, alpha=0.30)

# plot lines
plt.title("Sin and Cos")
plt.plot(y1, label = "Sinx")
plt.plot(y2, label = "Cosx")
plt.legend()
plt.grid(ls='--')
plt.show()
