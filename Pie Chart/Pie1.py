from matplotlib import pyplot as plt
import numpy as np
 
# Creating dataset
cars = ['Computer', 'Civil', 'Mechenical','Chemical', 'Automobile', 'Electrical']
 
data = [41, 17, 35, 29, 12, 23]
 
# Creating plot
fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = cars)
plt.title("Engineer in 2021") 

# show plot
plt.show()
