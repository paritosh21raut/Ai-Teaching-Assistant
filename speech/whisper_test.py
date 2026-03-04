import whisper

model = whisper.load_model("base")

def transcribe_audio(audio_path="output.wav"):
    print("Transcribing...")
    result = model.transcribe(audio_path, language="en")
    return result["text"]
