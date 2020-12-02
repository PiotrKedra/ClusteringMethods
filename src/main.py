import matplotlib.pyplot as plt
import pandas as pan

data = pan.read_csv('../resources/2d_dataset/r15.csv')


x = data[data.columns[0]]
y = data[data.columns[1]]
print(x)

plt.scatter(x, y)
plt.show()