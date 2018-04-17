import numpy as np
import matplotlib.pyplot as plt

modes = ['full', 'same', 'valid']
for m in modes:
    plt.plot(np.convolve(np.ones((200,)), np.ones((50,))/50, mode=m));
plt.axis([-10, 251, -.1, 1.1]);
plt.legend(modes, loc='lower center');
plt.show()