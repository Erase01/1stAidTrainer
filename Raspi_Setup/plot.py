from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from SerialRead import serRead

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

#fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

def animate(i):
    
    x_vals.append(next(index))
    y_vals.append(serRead())

    plt.cla()

    plt.plot(x_vals, y_vals, label='ECG')
    plt.legend(loc='upper left')
    
    plt.set_title('ECG')
    plt.set_xlabel('t')
    plt.set_ylabel('BPM')

    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.show()
