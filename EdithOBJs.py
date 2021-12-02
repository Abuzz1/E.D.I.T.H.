#TTS LIRBRAIES
from gtts import gTTS
import os

#TTS
class tts:
    def run(outBeta):
        vOut = gTTS(text = outBeta, lang = "en", slow = False)
        vOut.save(".voice.mp3")
        os.system("afplay " + ".voice.mp3")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


# GOOGLE SEARCH LIRBRAIES
import requests
from bs4 import BeautifulSoup
#GTTS
class ggs():
    def answer_search():
        result = ''
        user_query = input('Enter your query: ')

        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        ni = True

        if ni == True: # Answer 1
            try:
                result = soup.find(class_='Z0LcW').get_text()
                ni = False
            except:
                pass

        if ni == True: # Answer 2
            try:
                result = soup.find(class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf').get_text()
                ni = False
            except:
                pass

        if result == '':
            print("Restate the question")
            tts.run("Restate the question")
        else:
            print(result)
            tts.run(result)

    def disc_search():
        result = ''
        user_query = input('Enter your query: ')

        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        ni = True
        if ni == True:  # Description 1
            try:
                result = soup.find(class_='kno-rdesc').get_text()
                ni = False
            except:
                pass
        if ni == True:  # Description 2
            try:
                result = soup.find(class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf').get_text()
                ni = False
            except:
                pass

        if ni == True:  # Description 3
            try:
                result = soup.find(class_='LGOjhe').get_text()
                ni = False
            except:
                pass
        if result == '':
            print("Restate the question")
            tts.run("Restate the question")
        else:
            print(result)
            tts.run(result)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#



#WOLFRAMAI LIRBRAIES
import wolframalpha as wl
# wolframalpha api key
client = wl.Client("G8X7XT-LH93TX486J")

#WOLFRAMAI
class wolframAi(object):
    def run():
        while True:
            print("EDITH - wolframalpha")
            z = input("Query: ")
            if z == "exit" or z == "ex":
                break
            else:
                try:
                    wolfram_res = next(client.query(z).results).text
                    print("Wolfram Result:")
                    print()
                    print(wolfram_res)
                    tts.run(wolfram_res)
                except:
                    print("Wolfram can't find anything for this... try again or try the Wiki")
                    print()
                    break




# gui
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

# GUI INTERFACE
class WrappedLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            width=lambda *x:
            self.setter('text_size')(self, (self.width, None)),
            texture_size=lambda *x: self.setter('height')(self, self.texture_size[1]))

class edithGUI(App):
    txtBox = TextInput(multiline = True, padding_y = (20, 20), size_hint = (1, 0.5))
    out = WrappedLabel(text = "Output: ", font_size="15dp", color="#00FFCE", halign = "center")

    def build(self):
        # LAYOUTS
        mainLayout = BoxLayout(orientation="vertical")
        hboxLayout = BoxLayout(orientation="horizontal")

        img = Image(source="image-resources/edith-abuzz.png")

        wi = Button(text="wikipedia", background_color="#6FB1FC")
        ed = Button(text="edith.ai", background_color="#6FB1FC")
        wa = Button(text="wolframealpha", background_color="#6FB1FC")

        mainLayout.add_widget(img)
        wi.bind(on_press=self.wik)

        hboxLayout.add_widget(wi)
        ed.bind(on_press=self.edi)

        hboxLayout.add_widget(ed)
        #COMING SOON
        wa.bind(on_press=self.wfa)
        hboxLayout.add_widget(wa)

        vboxLayout = BoxLayout(orientation="vertical")

        vboxLayout.add_widget(self.txtBox)
        vboxLayout.add_widget(self.out)

        mainLayout.add_widget(hboxLayout)
        mainLayout.add_widget(vboxLayout)
        return mainLayout

    def wik(self, instance):
        # self.out.text = ""
        try:
            wiki_res = wiki.summary(self.txtBox.text, sentences=2)
            self.out.text = wiki_res
            tts.run(wiki_res)
        except:
            self.out.text = (
                "The Wiki can't find anything for this... try again or try Wolfram"
            )

    def edi(self, instance):
        self.out.text = "Edith AI coming soon.."

    def wfa(self, instance):
        try:
            wolfram_res = next(client.query(self.txtBox.text).results).text
            self.out.text = wolfram_res
            tts.run(wolfram_res)
        except:
            self.out.text = (
                "Wolfram can't find anything for this... try again or try the Wiki"
            )







# !!!!!!~


# for the colors in printing
class color:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    NORM = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
