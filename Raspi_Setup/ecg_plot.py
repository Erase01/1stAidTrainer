from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from SerialRead import serRead

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animate(i):
    x_vals.append(next(index))
    y_vals.append(serRead())

    plt.cla()

    plt.plot(x_vals, y_vals, label='ECG')
    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.show()
