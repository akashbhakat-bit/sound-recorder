import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
fs = 44100  # Sample rate
seconds = 5  # Duration of recording
print("record start")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2, dtype=np.int16)
sd.wait()  # Wait until recording is finished
print("record stop")
write('audio 2.wav', fs, myrecording)  # Save as WAV file 
