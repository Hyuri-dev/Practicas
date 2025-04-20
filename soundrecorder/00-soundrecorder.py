import sounddevice as sd
from scipy.io.wavfile import write

framerate = 44100 # Esta es la frecuencia de muestre

duration = 10

print("Recording ...")

record_voice = sd.rec(int(duration * framerate), samplerate = framerate , channels = 1)

sd.wait()

filename = input(f"ingrese un nombre para el archivo: ")

archivo = filename + ".wav"

write(archivo, framerate , record_voice)




