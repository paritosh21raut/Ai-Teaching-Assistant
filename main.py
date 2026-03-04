from core.query_processor import build_query
from core.retrieval import retrieve_wikipedia_data
from speech.whisper_test import transcribe_audio
from speech.audio_recorder import record_audio
from core.slide_renderer import show_slide

record_audio()  # This creates output.wav
speech_text = transcribe_audio()

query = build_query(speech_text)

print("\nSearch Query:")
print(query)

title, summary, image_url = retrieve_wikipedia_data(query)

if title is None:
    print("\nNo result found.")
else:
    print("\n=== Wikipedia Result ===")
    print("Title:", title)
    print("\nSummary:")
    print(summary)

    if image_url:
        print("\nImage URL:")
        print(image_url)

title, summary, image_path = retrieve_wikipedia_data(query)
show_slide(title, summary, image_path)
