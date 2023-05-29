from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from SerialRead import serRead

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

def animate(i):
    x_vals.append(next(index))
    y_vals.append(serRead())

    ax1.cla()

    ax1.plot(x_vals, y_vals, label='ECG')
    ax1.legend(loc='upper left')
    
    ax1.set_title('ECG')
    ax1.set_xlabel('t')
    ax1.set_ylabel('BPM')

    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.show()
