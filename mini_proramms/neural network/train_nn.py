import numpy as np
import matplotlib.pyplot as plt

N = 5

x1 = np.random.random(N)
x2 = x1 + [np.random.randint(10)/10 for i in range(N)]
Class1 = [x1, x2]

x1 = np.random.random(N)
x2 = x1 - [np.random.randint(10)/10 for i in range(N)] - 0.1
Class2 = [x1, x2]

f = [0, 1]

w = np.array([-0.7, 0.7])
for i in range(N):
    x = np.array([Class2[0][i], Class2[1][i]])
    y = np.dot(w, x)
    if y >= 0:
        print("Класс 1")
    else:
        print("Класс 2")

plt.scatter(Class1[0][:], Class1[1][:], s=10, c='red')
plt.scatter(Class2[0][:], Class2[1][:], s=10, c='blue')
plt.plot(f)
plt.grid(True)
plt.show()