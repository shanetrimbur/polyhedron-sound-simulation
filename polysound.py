import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Slider, Button
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import pygame

# Initialize pygame mixer for audio
pygame.mixer.init()

# Set up a list of 12 tones (one for each wall of the polyhedron)
tones = [pygame.mixer.Sound(f'tone_{i}.wav') for i in range(12)]  # Preloaded sound files for each wall

# Set up figure and 3D axis for plotting the polyhedron and bouncing spheres
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Create a dodecahedron (12-sided polyhedron)
vertices = np.array([
    [1, 1, 1], [-1, 1, 1], [1, -1, 1], [-1, -1, 1],
    [1, 1, -1], [-1, 1, -1], [1, -1, -1], [-1, -1, -1],
    [0, 0.618, 1.618], [0, -0.618, 1.618], [0, 0.618, -1.618], [0, -0.618, -1.618]
])

faces = [[0, 8, 9], [1, 8, 9], [2, 9, 10], [3, 10, 11], [0, 2, 4, 6], [1, 3, 5, 7]]

polyhedron = Poly3DCollection([vertices[face] for face in faces], alpha=0.25)
ax.add_collection3d(polyhedron)

# Ball positions, velocities, and radii
n_balls = 5
positions = np.random.uniform(-1, 1, (n_balls, 3))  # Initial random positions
velocities = np.random.uniform(-0.02, 0.02, (n_balls, 3))  # Initial random velocities
radii = np.random.uniform(0.05, 0.1, n_balls)  # Random radii for each ball

# Create gravity control variable
gravity_strength = 0

# Initialize ball scatter plot
ball_scatters = ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], s=200*radii, color='red')

# Callback function for sliders (rotation control and gravity control)
def update_rotation(val):
    ax.view_init(30, val)

def update_gravity(val):
    global gravity_strength
    gravity_strength = val

# Adding sliders for rotation and gravity, placed at the bottom for better visibility
ax_rot_slider = plt.axes([0.25, 0.08, 0.65, 0.03])
rotation_slider = Slider(ax_rot_slider, 'Rotation', 0, 360, valinit=0, valstep=1)
rotation_slider.label.set_fontsize(10)
rotation_slider.on_changed(update_rotation)

ax_grav_slider = plt.axes([0.25, 0.03, 0.65, 0.03])
gravity_slider = Slider(ax_grav_slider, 'Gravity', -1, 1, valinit=0, valstep=0.01)
gravity_slider.label.set_fontsize(10)
gravity_slider.on_changed(update_gravity)

# Spacing out the buttons and sliders for each wall control
button_axes = []
tone_sliders = []

# Adjust placement for better layout, placing sliders in two columns
for i in range(6):
    button_axes.append(plt.axes([0.05, 0.93 - i * 0.06, 0.1, 0.03]))  # Buttons on the left
    tone_sliders.append(plt.axes([0.18, 0.93 - i * 0.06, 0.2, 0.03]))  # Sliders next to buttons

for i in range(6, 12):
    button_axes.append(plt.axes([0.55, 0.93 - (i - 6) * 0.06, 0.1, 0.03]))  # Buttons on the right
    tone_sliders.append(plt.axes([0.68, 0.93 - (i - 6) * 0.06, 0.2, 0.03]))  # Sliders next to buttons

buttons = [Button(button_axes[i], f'Wall {i+1}', color="lightgray") for i in range(12)]
sliders = [Slider(tone_sliders[i], f'Tone {i+1}', 0.1, 2, valinit=1) for i in range(12)]

# Function to adjust tone pitch based on sliders
def adjust_pitch(i, val):
    tones[i].set_volume(val)

for i, slider in enumerate(sliders):
    slider.label.set_fontsize(8)
    slider.on_changed(lambda val, i=i: adjust_pitch(i, val))

# Update function for the animation
def update_balls(frame):
    global velocities, positions
    # Update ball positions
    positions += velocities

    # Apply gravity effect
    velocities[:, 1] -= gravity_strength * 0.001

    # Check for collisions with polyhedron walls (simple detection)
    for i in range(n_balls):
        for j, face in enumerate(faces):
            normal = np.mean(vertices[face], axis=0)
            if np.dot(positions[i], normal) > 1:  # Simple collision detection
                velocities[i] *= -1  # Bounce back
                tones[j].play()  # Play corresponding tone

    # Update scatter object instead of recreating it
    ball_scatters._offsets3d = (positions[:, 0], positions[:, 1], positions[:, 2])

    return ball_scatters,

# Animate the balls
ani = animation.FuncAnimation(fig, update_balls, frames=200, interval=20, blit=False)

# Show plot
plt.show()
