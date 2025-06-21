import sounddevice as sd
import numpy as np

def callback(indata, frames, time, status):
    if status:
        print(status)
    volume = np.linalg.norm(indata) * 10
    print(f"Volume level: {volume:.2f}")

# Set sampling rate and channels properly
with sd.InputStream(callback=callback, samplerate=44100, channels=1):
    print("Listening... Press Ctrl+C to stop.")
    sd.sleep(10000)  # 10 seconds
