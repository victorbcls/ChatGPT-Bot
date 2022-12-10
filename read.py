import random
import string

from gtts import gTTS
from langdetect import detect

language = "pt-br"


def readAndSave(text):
    try:
        language = detect(text)
        if language == "pt":
            language = "pt-br"
    except:
        language = "pt-br"
    audio = gTTS(
        text=text,
        lang=language,
        slow=False,
        tld="com.br",
    )
    letters = string.ascii_uppercase
    fileName = "./mp3/" + ("".join(random.choice(letters) for i in range(10))) + ".mp3"
    audio.save(fileName)
    return fileName
