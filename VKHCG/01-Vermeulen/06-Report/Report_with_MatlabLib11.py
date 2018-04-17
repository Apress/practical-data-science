import matplotlib.pyplot as plt
from numpy.random import randn
z = randn(8)
plt.figure(figsize=(15, 5))
red_dot, = plt.plot(z, "ro-", markersize=18)
white_cross, = plt.plot(z[:5], "w+", markeredgewidth=3, markersize=15)
black_cross, = plt.plot(z[:2], "y+", markeredgewidth=3, markersize=15)
plt.legend([red_dot, (red_dot, white_cross),(red_dot,black_cross)],\
            ["Krennwallner", "Clark","Hillman"])