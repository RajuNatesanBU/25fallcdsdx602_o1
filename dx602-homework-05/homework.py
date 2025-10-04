import numpy as np
import matplotlib.pyplot as plt
import csv

print(np.__version__)
print(np.__file__)

q8a_x = [1, 2, 3, 4, 5]
q8a_y = [1, 2, 3, 2, 1]

q8b_x = [-2, -1, 0, 1, 2]
q8b_y = [5, 3, 1, 3, 5]

q8c_x = [0, 2, 4, 6, 8]
q8c_y = [5, 4, 3, 2, 1]

x_lim = q8a_x + q8b_x + q8c_x
y_lim = q8a_y + q8b_y + q8c_y

x_min, x_max = min(x_lim), max(x_lim)
y_min, y_max = min(y_lim), max(y_lim)

plt.figure(figsize=(15, 5))
for i in range(1, 4):
    plt.subplot(1, 3, i)
    if i == 1:
        plt.plot(q8a_x, q8a_y)
    elif i == 2:
        plt.plot(q8b_x, q8b_y)
    else:
        plt.plot(q8c_x, q8c_y)
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

plt.subplots_adjust(hspace=1.0, wspace=0.4)

#plt.show()