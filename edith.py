# backend and frontend support for edith.

# Import line
import os
from os import error
from os import system, name
import os.path
import requests
from bs4 import BeautifulSoup
import webbrowser
import time
import sys

# gui
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

# CLASSES TTS GGS WOLFRAMAI
from EdithOBJs import tts, ggs, wolframAi

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


# Welcome init
print("Welcome")
for x in range(20):
    print(color.FAIL + "#")
    time.sleep(0.01)
for x in range(50):
    print(color.OKCYAN + "#")
for x in range(30):
    time.sleep(0.01)
    print(color.OKGREEN + "#")
    time.sleep(0.01)

# assistant interface
def assistant():
    y = input("gui or terminal: ")
    if y == "gui":
        gui()
    elif y == "terminal" or y == "term":
        txtVersion()
    else:
        print("try again!")
        print()
        assistant()


# text version of assistant interface ai
def txtVersion():
    while True:
        q = input("Do you want to try wolframAi or search? ")
        if q == "wolframAi" or q == "wolframai" or q == "wa" or q == "wA":
            wolframAi.run()
        elif q == "search" or q == "sc":
            i = input("answer of descr? ")
            if i == "descr" or i == "d":
                ggs.disc_search()
            elif i == "answer":
                ggs.answer_search()
        elif q == "exit" or q == "ex" or q == "clear":
            clear()
        else:
            print("try again")
            txtVersion()


# gui ai
def gui():
    if __name__ == "__main__":
        window = edithGUI()
        window.run()


# clears space
def clear():
    _ = system("clear")
    main()


# pulls random wikipedia pages to choose
def randomwiki():
    while True:
        # Getting Wiki's random URL page and finding the title
        url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        soup = BeautifulSoup(url.content, "html.parser")
        title = soup.find(class_="firstHeading").text

        # i/o input
        print(f"{title} \nDo you want to view it? (Y/N)")
        ans = input("").lower()

        # i/o output
        if ans == "y" or ans == "Y":
            url = "https://en.wikipedia.org/wiki/%s" % title
            webbrowser.open(url)
            break
        elif ans == "n" or ans == "N":
            print("Try again!")
            continue
        elif ans == "clear" or ans == "exit" or ans == "ex":
            clear()
        else:
            print("ERROR!")
            print("RETRY!")
            break


# Main run loop to run everything.
def main():
    print(
        color.NORM
        +
    """
    █▀▀ █▀▄ █ ▀█▀ █ █
    ██▄ █▄▀ █  █  █▀█
    """
    )

    print(
        color.NORM
        + "Welcome to "
        + color.BOLD
        + "E.D.I.T.H. "
        + color.NORM
        + "("
        + color.FAIL
        + "Abuzz-Industies"
        + color.NORM
        + ")"
    )

    print(
        "Terminal commands: "
        + color.OKGREEN
        + "clear"
        + color.NORM
        + "; "
        + color.OKGREEN
        + "exit"
        + color.NORM
    )
    print(
        "BRANCH ACCSESS: "
        + color.OKGREEN
        + "assistant"
        + color.NORM
        + "; "
        + color.OKGREEN
        + "randomwiki"
        + color.NORM
    )

    while True:
        i = input("branch: ")
        if i == "assistant" or i == "as":
            assistant()
        elif i == "clear":
            clear()
        elif i == "randomwiki":
            randomwiki()
        elif i == "exit" or i == "ex":
            _ = system("clear")
            sys.exit()
        else:
            print("!error! ~ !retry!")
main()
# This is pretty neat :D Ali Alshawabkeh
