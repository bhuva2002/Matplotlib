import matplotlib.pyplot as plt
#import numpy as np

#xpoints = np.array([1995,2000,2005,2010,2015,2020])
#ypoints = np.array([5,17,50,76,113,563])

xpoints=[1995,2000,2005,2010,2015,2020]
ypoints=[5,17,50,76,113,563]

plt.plot(xpoints, ypoints, marker='o', ls='-.', color='r')

plt.title("Groth of amazon.com")
plt.xlabel("Year")
plt.ylabel("Valuation(in billion)")

plt.grid(linestyle = '--')
plt.show()

