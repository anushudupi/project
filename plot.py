import numpy as np
import matplotlib.pyplot as plt

# Define the length of the data array
n = 1000

# Initialize the plot
fig, ax = plt.subplots()
line, = ax.plot(np.zeros(n),"y")

# Set the axis labels and title
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.set_title('Digital Oscilloscope')

# Set the axis limits
ax.set_ylim(-1.1, 1.1)
ax.set_xlim(0, n)

# Draw the plot and cache the renderer
fig.canvas.draw()
#background = fig.canvas.copy_from_bbox(ax.bbox)
print(ax.bbox)

# Start an infinite loop to continuously update the plot
while True:
    # Generate a sine wave data with frequency of 1Hz
    data = np.random.uniform(-1, 1, n)
    
    # Update the plot
    line.set_ydata(data)
    #fig.canvas.restore_region(background)
    #ax.draw_artist(line)
    #fig.canvas.blit(ax.bbox)
    
    # Pause for a short time to simulate real-time data acquisition
    plt.pause(0.1)
