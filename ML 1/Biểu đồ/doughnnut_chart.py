import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
ax.axis('equal')
width = 0.3

# Outer ring
cm = plt.get_cmap("tab20c")
cout = cm(np.arange(3)*4)
pie, _ = ax.pie([120,77,39], radius=1, labels=list("ABC"), colors=cout)
plt.setp(pie, width=width, edgecolor='white')

# Inner ring
cin = cm(np.array([1,2,5,6,9,10]))
labels = list(map("".join, zip(list("aabbcc"),map(str, [1,2]*3))))
pie2, _ = ax.pie([60,60,37,40,29,10], radius=1-width, labels=labels,
                 labeldistance=0.7, colors=cin)
plt.setp(pie2, width=width, edgecolor='white')
plt.show()  