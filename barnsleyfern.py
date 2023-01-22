import random
import matplotlib.pyplot as plt

x = []
y = []
x.append(0)
y.append(0)
pc = 0
lc = 0
curr = 0

for z in range(200000):

    choice = random.randint(1,100)

    if choice == 1:
        x.append(0)
        y.append(0.16 * (y[curr]))
    if choice >= 2 and choice <= 86:
        x.append(0.85 * (x[curr]) + 0.04 * (y[curr]))
        y.append(-0.04 * (x[curr]) + 0.85 * (y[curr]) + 1.6)
    if choice >= 94 and choice <= 100:
        x.append(-0.15 * (x[curr]) + 0.28 * (y[curr]))
        y.append(0.26 * (x[curr]) + 0.24 * (y[curr]) + 0.44)
    if choice >= 87 and choice <= 93:
        x.append(0.2 * (x[curr]) - 0.26 * (y[curr]))
        y.append(0.23 * (x[curr]) + 0.22 * (y[curr]) + 1.6)
    curr += 1

plt.scatter(x, y, s = 0.2, edgecolor= 'black')
plt.show()