from matplotlib import pyplot as plt
import numpy as np
 
 
# Creating dataset
a = np.array([22, 1, 100, 43, 73, 55, 8, 11, 20, 4])
 
# Creating histogram
figure, ax = plt.subplots(figsize =(10, 10))
ax.hist(a, bins = [0, 20, 40, 60, 80, 100])
plt.title("Histogram", fontsize=20)
 
# Show plot
plt.show()
