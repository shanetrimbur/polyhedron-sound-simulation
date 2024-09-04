import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')  # Set background to black for contrast
ax.axis('off')  # Hide the axis for a cleaner look

# Parameters
n_circles = 20  # Number of circles along one axis
max_radius = 0.05  # Max radius of circles
min_radius = 0.01  # Min radius of inner circles
center_radius = 0.2  # Max radius of central circles

# Create a grid of positions
x = np.linspace(-1, 1, n_circles)
y = np.linspace(-1, 1, n_circles)
xx, yy = np.meshgrid(x, y)

# Calculate distances from the center for each circle
distances = np.sqrt(xx**2 + yy**2)
max_distance = np.max(distances)

# Normalize distances for outer circle radii
outer_radii = max_radius - (max_radius - min_radius) * (distances / max_distance)

# Create the circles and add them to the plot
outer_circles = []
inner_circles = []
center_circles = []

# Add outer circles and inner circles to the plot
for i in range(n_circles):
    for j in range(n_circles):
        # Outer circle
        outer_circle = plt.Circle((xx[i, j], yy[i, j]), outer_radii[i, j], color='white', fill=False, lw=1)
        ax.add_artist(outer_circle)
        outer_circles.append(outer_circle)

        # Inner circle (starting small)
        inner_circle = plt.Circle((xx[i, j], yy[i, j]), 0.0, color='red', fill=True, alpha=0.7)
        ax.add_artist(inner_circle)
        inner_circles.append(inner_circle)

# Add central competing circles (cells) at the center
for i in range(4):  # Create 4 competing central circles
    central_circle = plt.Circle((0, 0), radius=np.random.uniform(0.05, center_radius),
                                color=np.random.rand(3,), fill=True, alpha=0.7)
    ax.add_artist(central_circle)
    center_circles.append(central_circle)

# Animation update function
def update(frame):
    # Update the inner circles to grow until they cancel out (reach the size of the outer circle)
    for i, inner_circle in enumerate(inner_circles):
        # Calculate growth factor based on the current frame
        growth_factor = np.abs(np.sin(frame / 20.0))  # Sinusoidal growth/shrink effect
        inner_circle.set_radius(outer_radii.flatten()[i] * growth_factor)

    # Update the central competing circles
    for i, center_circle in enumerate(center_circles):
        # Randomly adjust the size to simulate competition for space
        current_radius = center_circle.get_radius()
        delta_radius = np.random.uniform(-0.01, 0.02)  # Small random growth/shrink
        new_radius = max(0.05, min(center_radius, current_radius + delta_radius))  # Ensure it stays within bounds
        center_circle.set_radius(new_radius)

    return inner_circles + center_circles

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=False)

# Show the animation
plt.show()
