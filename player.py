import soundfile as sf;
import sounddevice as sd;

data , fs = sf.read("recording.wav");

sd.play(data, fs);
sd.wait();
print("finished");