# backend support for edith.

#Import line
import os
from os import error
from os import system, name
import os.path
import wolframalpha as wl
import wikipedia as wiki
import requests
from bs4 import BeautifulSoup
import webbrowser
import time
import sys
#gui
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


#wolframalpha api key
client = wl.Client("G8X7XT-LH93TX486J")

# GUI INTERFACE
class edithGUI(App):
    def build(self):
        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 2
        self.window.rows = 4
        self.window.size_hint = (1, 1)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}


        # logo
        self.window.add_widget(Image(source="image-resources/edith-abuzz.png"))


        # label widget
        self.greeting = Label(
                        text= "What's your name?",
                        font_size= 18,
                        color= '#00FFCE'
                        )
        self.window.add_widget(Label(
                        text = "QUICK COMMANDS:",
                        font_size = 35,
                        color = '#00FFCE'
                        ))



        self.window.add_widget(self.greeting)

        self.window.add_widget(Label(
                        text = "QUICK COMMANDS:",
                        font_size = 35,
                        color = '#00FFCE'
                        ))



        # text input widget
        self.user = TextInput(
                    multiline= False,
                    padding_y= (20,20),
                    size_hint= (1, 0.5)
                    )

        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
                      text= "GREET",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#00FFCE',
                      #remove darker overlay of background colour
                      # background_normal = ""
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        # change label text to "Hello + user name!"
        self.greeting.text = "Hello " + self.user.text + "!"


class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    NORM = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Welcome init
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
print(color.NORM + """
█▀▀ █▀▄ █ ▀█▀ █░█
██▄ █▄▀ █ ░█░ █▀█
""")
print()
print(color.NORM + "Welcome to " + color.BOLD + "E.D.I.T.H. " + color.NORM + "(" + color.FAIL + "Abuzz-Industies" + color.NORM + ")")

#assistant interface
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
        q = input("Do you want to try wolframAi or the wiki; or both! ")
        if q == "wolframAi" or q == "wolframai" or q == "wa" or q == "wA":
            wolframAi()
        elif q == "wiki" or q == "wik":
            wikiAi()
        elif q == "both" or q == "Both":
            bothText()
        elif q == "exit":
            clear()
        else:
            print("try again")
            txtVersion()
# both WikiAi and wolframAi interface
def bothText():
    while True:
        print("EDITH")
        z = input("Query: ")
        if z == "exit" or z == "ex":
            clear()
        else:
            try:
                wiki_res = wiki.summary(z, sentences=2)
                wolfram_res = next(client.query(z).results).text
                print("Wolfram Result: ", wolfram_res)
                print("Wikipedia Result: ", wiki_res)
            except wiki.exceptions.DisambiguationError:
                wolfram_res = next(client.query(z).results).text
                print("Wolfram Result: ", wolfram_res)
            except wiki.exceptions.PageError:
                wolfram_res = next(client.query(z).results).text
                print("Wolfram Result: ", wolfram_res)
            except:
                wiki_res = wiki.summary(z, sentences=2)
                print("Wikipedia Result: ", wiki_res)

# WikiAi interface
def wikiAi():
    while True:
        print("EDITH - wikipedia")
        z = input("Query: ")
        if z == "exit" or z == "ex":
            clear()
        else:
            try:
                wiki_res = wiki.summary(z, sentences=2)
                print("Wikipedia Result: ", wiki_res)
            except:
                print("The Wiki can't find anything for this... try again or try Wolfram")
                q == "wolframAi"
                txtVersion()

# wolframAi interface
def wolframAi():
    while True:
        print("EDITH - wolframalpha")
        z = input("Query: ")
        if z == "exit" or z == "ex":
            clear()
        else:
            try:
                wolfram_res = next(client.query(z).results).text
                print("Wolfram Result: ", wolfram_res)
            except:
                print("Wolfram can't find anything for this... try again or try the Wiki")
                print()
                txtVersion()




# gui ai
def gui():
    if __name__ == "__main__":
        edithGUI().run()



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
        else:
            print("ERROR!")
            print("RETRY!")
            break

#Main run loop to run everything.
def main():
    print()
    print("Terminal commands: " +  color.OKGREEN + "clear" + color.NORM + "; " + color.OKGREEN + "exit" + color.NORM)
    print("BRANCH ACCSESS: " +  color.OKGREEN + "assistant"  + color.NORM + "; " + color.OKGREEN + "randomwiki" + color.NORM)
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
