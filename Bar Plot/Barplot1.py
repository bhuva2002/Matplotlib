import numpy as np
import matplotlib.pyplot as plt
 
# creating the dataset
data = {'1':20, '2':15, '3':1, '4':5, '5':7, '6':8, '7':6, '8':12, '9':23, '10':11}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize=(8,5))
 
# creating the bar plot
plt.bar(courses, values, color ='blue', width = 0.6)

plt.xlabel("Overs",color='r',fontname="Gabriola",fontsize=16)
plt.ylabel("Runs",color='r',fontname="Gabriola",fontsize=16)
plt.title("Runs per over",fontsize=20,color='g',fontname="Times New Roman")
plt.show()
