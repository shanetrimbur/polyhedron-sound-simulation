import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')  # Hide the axis for a cleaner look

# Function to create a random color
def random_color():
    return np.random.rand(3,)

# Create some abstract shapes (circles, polygons, lines, etc.)
shapes = []

# Adding circles
for i in range(5):
    circle = plt.Circle((np.random.uniform(1, 9), np.random.uniform(1, 9)), 
                        radius=np.random.uniform(0.5, 1.5), 
                        color=random_color(), 
                        fill=True, alpha=0.6)
    shapes.append(circle)
    ax.add_artist(circle)

# Adding rectangles
for i in range(5):
    rectangle = patches.Rectangle((np.random.uniform(1, 9), np.random.uniform(1, 9)), 
                                  width=np.random.uniform(0.5, 2), 
                                  height=np.random.uniform(0.5, 2), 
                                  angle=np.random.uniform(0, 360), 
                                  color=random_color(), alpha=0.6)
    shapes.append(rectangle)
    ax.add_patch(rectangle)

# Adding polygons
for i in range(5):
    polygon = patches.RegularPolygon((np.random.uniform(1, 9), np.random.uniform(1, 9)), 
                                     numVertices=np.random.randint(3, 6), 
                                     radius=np.random.uniform(0.5, 1.5), 
                                     orientation=np.random.uniform(0, np.pi), 
                                     color=random_color(), alpha=0.6)
    shapes.append(polygon)
    ax.add_patch(polygon)

# Adding lines
for i in range(5):
    x = np.random.uniform(1, 9, 2)
    y = np.random.uniform(1, 9, 2)
    line, = ax.plot(x, y, color=random_color(), lw=np.random.uniform(1, 3))
    shapes.append(line)

# Animation update function
def update(frame):
    for shape in shapes:
        if isinstance(shape, patches.Circle):
            # Change position or radius for circles
            shape.set_center((np.random.uniform(1, 9), np.random.uniform(1, 9)))
            shape.set_radius(np.random.uniform(0.5, 1.5))
        elif isinstance(shape, patches.Rectangle):
            # Change position or rotation for rectangles
            shape.set_xy((np.random.uniform(1, 9), np.random.uniform(1, 9)))
            shape.set_angle(np.random.uniform(0, 360))
        elif isinstance(shape, patches.RegularPolygon):
            # Change position for polygons using `xy` attribute
            shape.xy = (np.random.uniform(1, 9), np.random.uniform(1, 9))
        elif isinstance(shape, plt.Line2D):
            # Change line endpoints for lines
            shape.set_data(np.random.uniform(1, 9, 2), np.random.uniform(1, 9, 2))

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=500, repeat=True)

# Show animation
plt.show()
