from gtts import gTTS
from pydub import AudioSegment
import os

# List of words and their translations
words = [

]

# Folder for storing temporary MP3 files
if not os.path.exists("translation/english"):
    os.makedirs("translation/english")

# Create MP3 files for each word
for i, (english_word, russian_word) in enumerate(words):
    # Generate MP3 for English word UK
    tts_eng = gTTS(text=english_word, lang='en', tld='co.uk')
    eng_file = f"translation/english/eng_uk_{i}.mp3"
    tts_eng.save(eng_file)

    # Generate MP3 for English word US
    tts_eng = gTTS(text=english_word, lang='en', tld='us')
    eng_file = f"translation/english/eng_us_{i}.mp3"
    tts_eng.save(eng_file)


    # MP3 generation for Russian words
    tts_rus = gTTS(text=russian_word, lang='ru')
    rus_file = f"translation/english/rus_{i}.mp3"
    tts_rus.save(rus_file)

    combined = AudioSegment.empty()

    eng_uk_file = f"translation/english/eng_uk_{i}.mp3"
    eng_us_file = f"translation/english/eng_us_{i}.mp3"
    rus_file = f"translation/english/rus_{i}.mp3"

    # Download and add an English file
    combined += AudioSegment.from_file(eng_us_file)
    combined += AudioSegment.from_file(eng_uk_file)
    # Upload and add Russian file
    combined += AudioSegment.from_file(rus_file)

    # Delete temporary files
    os.remove(f"translation/english/eng_uk_{i}.mp3")
    os.remove(f"translation/english/eng_us_{i}.mp3")
    os.remove(f"translation/english/rus_{i}.mp3")

    # Save combined file
    combined.export(f"translation/english/{english_word}.mp3", format="mp3")

print("MP3 recordings successfully created")
