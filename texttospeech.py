from gtts import gTTS
import os
import tempfile

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
        tts.save(temp_file.name)
        os.startfile(temp_file.name)

# Example usage
text_to_speech("Hello, how are you today?")
