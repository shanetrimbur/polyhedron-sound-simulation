# Polyhedron Bouncing Balls with Interactive Sounds 🎵

## Description

This project is an interactive 3D simulation where multiple balls bounce around inside a polyhedron (a dodecahedron in this case). Each ball interacts with the polyhedron's walls, and when they hit a wall, they play an assigned sound. The project uses Python, Matplotlib, and Pygame to create a visually appealing and sonically interactive experience. 

You can control the rotation of the polyhedron, gravity strength, and even the sound pitch that plays when the balls hit a wall using intuitive sliders and buttons. This creates a dynamic audio-visual experience where users can experiment with how sound and visuals interact in real-time.

## Features

- **3D Polyhedron Simulation**: Watch balls bounce around a 3D polyhedron with real-time gravity and wall collisions.
- **Interactive Audio**: Each time a ball hits a polyhedron wall, a sound is triggered. You can adjust the pitch of the sounds using sliders.
- **Control Gravity**: Adjust the gravity in the simulation using a slider, making balls bounce higher or fall faster.
- **Rotation Control**: Rotate the polyhedron using a slider to view it from different angles.
- **Customizable Sounds**: Each of the 12 polyhedron walls has its own sound, and the pitch can be customized using sliders.
- **Responsive Design**: Buttons and sliders are arranged for easy interaction and real-time control of the simulation.

## Installation

To get the project running on your local machine, follow these steps:

### Prerequisites

1. **Python 3.x**: Make sure Python 3.x is installed on your system.
2. **Pip**: Ensure `pip` is installed.
3. **Pygame**: Used for handling sounds.
4. **Matplotlib**: For creating the 3D polyhedron and animation.
5. **Numpy**: For managing vectors, positions, and velocities in the simulation.

### Installation Steps

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/polyhedron-sound-simulation.git
    cd polyhedron-sound-simulation
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have the correct sound files (`tone_0.wav` to `tone_11.wav`) in the working directory. These are triggered when balls hit the polyhedron walls.

4. Run the program:
    ```bash
    python3 polysound.py
    ```

## Usage

- **Rotate the Polyhedron**: Use the "Rotation" slider at the bottom to rotate the polyhedron in real-time.
- **Control Gravity**: The "Gravity" slider lets you increase or decrease gravity.
- **Adjust Sound Pitch**: Each polyhedron wall has its own button and pitch slider. You can adjust the pitch for each wall sound by moving the slider next to its button.
- **Experiment with Sound**: When a ball hits a wall, you will hear a sound. Try adjusting the sliders to explore how the pitches change.

## Future Improvements and Ideas for Iteration 🚀

- **Add More Shapes**: Support for more polyhedrons (e.g., icosahedron, tetrahedron) for diverse geometric visuals.
- **Ball-to-Ball Collisions**: Currently, only wall collisions are handled. Future versions can include ball-to-ball collisions to make the interaction even more dynamic.
- **Real-time Audio Synthesis**: Rather than using pre-recorded audio files, implement real-time audio synthesis for more interactive and customizable soundscapes.
- **Enhanced Visuals**: Add shading, lighting, or textures to the polyhedron and balls for a more immersive 3D experience.
- **Save Settings**: Allow users to save their slider settings (gravity, rotation, pitch) for future sessions.
- **Custom Sound Upload**: Enable users to upload their own sound files for each wall to create a personalized audio experience.
- **Mobile/Touch Controls**: Extend the interface for mobile devices with touch-based controls for sliders and polyhedron rotation.
- **Networked Interaction**: Create a networked version where multiple users can control the polyhedron or sounds from different devices.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy bouncing and sound exploring! 🎶🎨
