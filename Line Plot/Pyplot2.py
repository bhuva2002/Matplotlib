import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x,y)
plt.xlabel("Month")
plt.ylabel("Rupees(in 10000)")
plt.title("Sales",fontsize=18,color='g')
plt.grid(linestyle = '--')
plt.plot(x, y, marker='o', ls='-.', color='r')

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y)
plt.xlabel("Month")
plt.ylabel("Rupees(in 10000)")
plt.title("Income",fontsize=18,color='g')
plt.grid(linestyle = '--')
plt.plot(x, y, marker='o', ls='-.', color='r')

plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.5, hspace=0.7)
                    
plt.suptitle("Pramukh Book Store",fontsize=22,color='b')

plt.tight_layout()
plt.subplots_adjust(top=0.84)
plt.show()
