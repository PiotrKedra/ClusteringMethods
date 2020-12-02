import matplotlib.pyplot as plt
import pandas as pan

data = pan.read_csv('../../resources/2d_dataset/r15.png')


x = data[data.columns[0]]
y = data[data.columns[1]]
print(x)

x_np = x.to_numpy()

plt.scatter(x, y)
plt.show()