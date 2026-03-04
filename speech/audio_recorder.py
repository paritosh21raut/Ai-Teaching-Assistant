import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename="output.wav", duration=5, sample_rate=16000):
    print("Recording for 5 seconds...")
    
    audio = sd.rec(int(duration * sample_rate),
                   samplerate=sample_rate,
                   channels=1,
                   dtype='int16')

    sd.wait()
    write(filename, sample_rate, audio)

    print(f"Saved as {filename}")
