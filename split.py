import scipy.io.wavfile as wf

audio = 'Bahan_Final_PA/Motorcycle_noise_80db0.wav'

sr, aud = wf.read(audio)
print(sr)
n = 0
frame = 1600 # 0,2 s

for i in range(276):
	filename = 'Samples/Motorcycle_Engine/'+str(i+1+1104) + ".wav"
	new_aud = aud[(i*frame):(i*frame)+(frame*25)]
	idx = str(i+1) + " " + str(new_aud.shape)
	wf.write(filename,sr,new_aud)
	print(filename)