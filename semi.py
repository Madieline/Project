#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Define the coordinates for the irregular shape (route)
x_coords = [15, 10, 10, 10, 8, 8, 11, 11, 12.5, 14.5, 15, 15]
y_coords = [1, 1, 3, 4, 4, 4.5, 4.5, 5, 5, 5, 5, 1]

# Define the coordinates and labels for the places (markers)
place_coords = [(15, 1), (10, 3), (8, 4), (11, 4.5), (12.5, 5), (14.5, 5)]
place_labels = ['Hagdang Bato', 'LS Covered Courts', 'Ateneo Grade School', 'Diversion Road', 'Leong Hall', 'Xavier Hall']

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the entire route line
ax.plot(x_coords, y_coords, color='lightgray', label='Other Routes')  # Light gray for other routes

# Load the pin icon image
icon_path = 'pin.png'  # Replace with your pin icon path
icon = plt.imread(icon_path)

# Plot the markers with pin icons and labels
for (x, y), label in zip(place_coords, place_labels):
    im = OffsetImage(icon, zoom=0.005)  # Assuming 'icon' is defined as in previous examples
    ab = AnnotationBbox(im, (x, y), xycoords='data', frameon=False)
    ax.add_artist(ab)
    ax.text(x + 0.1, y + 0.2, f' {label}', fontsize=8, verticalalignment='center_baseline', zorder=10)

# Function to highlight a specific route dynamically
def highlight_route(start, end):
    start_index = place_labels.index(start)
    end_index = place_labels.index(end)
    ax.plot(x_coords[start_index:end_index+1], y_coords[start_index:end_index+1], color='red', label=f'Route {start} to {end}')
    ax.legend()

# Example of dynamically highlighting a route (replace with your logic)
highlight_route('Hagdang Bato', 'Ateneo Grade School')

# Customize the plot
ax.set_title('Line A Route', fontsize=14, pad=20)  # Increase the font size of the title to 14 and pad with 20 points
ax.axis('off')  # Turn off the axis

# Adjust plot limits to fit markers and icons
ax.set_xlim(min(x_coords) - 1, max(x_coords) + 1)
ax.set_ylim(min(y_coords) - 1, max(y_coords) + 1)

# Show the plot
plt.show()

