import matplotlib.pyplot as plt
from RandomWalk.random_walk import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk()

plt.plot(rw.x_values, rw.y_values, c='red', linewidth=1)

plt.show()
