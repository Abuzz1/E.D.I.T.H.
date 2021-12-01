from gtts import gTTS
import os
class tts:
    def run(outBeta):
        vOut = gTTS(text = outBeta, lang = "en", slow = False)
        vOut.save(".voice.mp3")
        os.system("afplay " + ".voice.mp3")
