import sounddevice as sd; # to communicate with the microphone
from scipy.io.wavfile  import write;

sample_rate = 44100; # Sample rate
duration = 6;
print("Recording...")
audio = sd.rec(int(duration * sample_rate), samplerate = sample_rate, channels=1, dtype="int16")

sd.wait() # Wait until recording is finished
 
write("recording.wav", sample_rate, audio)
print("Saved recording.wav")

