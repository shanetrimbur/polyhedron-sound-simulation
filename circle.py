import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('blue')  # Set background to blue
ax.axis('off')  # Hide the axis for a cleaner look

# Parameters
n_circles = 20  # Number of circles along one axis
max_radius = 0.05  # Max radius of circles
min_radius = 0.01  # Min radius of circles

# Circle properties (positions and radii)
circles = []
positions = []
velocities = []
radii = []

# Generate random positions, velocities, and radii for each circle
for i in range(n_circles):
    x_pos, y_pos = np.random.uniform(-1, 1, 2)
    vx, vy = np.random.uniform(-0.01, 0.01, 2)  # Random velocities for motion
    radius = np.random.uniform(min_radius, max_radius)
    
    # Create circle
    circle = plt.Circle((x_pos, y_pos), radius, color='red' if i % 2 == 0 else 'white')
    ax.add_artist(circle)
    circles.append(circle)
    positions.append([x_pos, y_pos])
    velocities.append([vx, vy])
    radii.append(radius)

positions = np.array(positions)
velocities = np.array(velocities)
radii = np.array(radii)

# Mouse tracking
mouse_position = np.array([0.0, 0.0])

# Event handler to track mouse movement
def on_mouse_move(event):
    if event.xdata is not None and event.ydata is not None:
        mouse_position[0] = event.xdata
        mouse_position[1] = event.ydata

# Add the event listener for mouse movement
cid = fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)

# Update function for the animation
def update(frame):
    # Update each circle's position based on velocity
    for i, circle in enumerate(circles):
        # Update position
        positions[i] += velocities[i]

        # Boundary check to keep circles within the window
        if positions[i][0] - radii[i] < -1 or positions[i][0] + radii[i] > 1:
            velocities[i][0] *= -1  # Reverse X velocity if hitting boundary
        if positions[i][1] - radii[i] < -1 or positions[i][1] + radii[i] > 1:
            velocities[i][1] *= -1  # Reverse Y velocity if hitting boundary

        # Set new position
        circle.set_center(positions[i])

        # Interaction with mouse: circles "bump" away from the mouse
        distance_to_mouse = np.linalg.norm(positions[i] - mouse_position)
        if distance_to_mouse < 0.3:  # If mouse is near the circle
            direction_away_from_mouse = positions[i] - mouse_position
            direction_away_from_mouse /= np.linalg.norm(direction_away_from_mouse)
            velocities[i] += 0.01 * direction_away_from_mouse  # Increase velocity away from the mouse
    
    return circles

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=30, blit=False)

# Show the animation
plt.show()
