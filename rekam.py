import sounddevice as sd
import scipy.io.wavfile as wf

duration = 60  # seconds
fs = 8000
aud = sd.rec(int(duration * fs), samplerate=fs, channels=2)
print(aud.shape)
sd.wait()
wf.write('Silent',8000,aud)