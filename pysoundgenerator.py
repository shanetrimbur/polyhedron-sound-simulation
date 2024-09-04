import numpy as np
from scipy.io.wavfile import write

# Function to generate a tone
def generate_tone(frequency, duration=1.0, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = 0.5 * np.sin(2 * np.pi * frequency * t)
    return tone

# Save 12 different tones (frequencies between 200Hz and 800Hz)
for i in range(12):
    frequency = 200 + i * 50  # Different frequencies for each tone
    tone = generate_tone(frequency)
    write(f'tone_{i}.wav', 44100, (tone * 32767).astype(np.int16))  # Save as 16-bit WAV
