import os
from os import error
from os import system, name
import wolframalpha as wl
import wikipedia as wiki
import PySimpleGUI as sg
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import webbrowser
import time
from dotenv import load_dotenv

load_dotenv()

api = os.enviorn['API_CODE']

client = wl.Client(api)

print("Welcome")
for x in range(100):
    print("#")
    time.sleep(.01)
print("Welcome to E.D.I.T.H. (Abuzz-Industies)")


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('E.D.I.T.H. GUI % Stark Industries')],
            [sg.Text('Enter query'), sg.InputText()],
            [sg.Button('Submit')] ]

def text():
    y = input('gui or terminal: ')
    if y == 'gui':
        gui()
    elif y == 'terminal':
        txtVersion()
    else:
        print("try again!")
        print()
        text()

def txtVersion():
    print("EDITH")
    z = input('Query: ')
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

def gui():
    try:
        # Create the Window
        window = sg.Window('EDITH', layout)
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            try:
                wiki_res = wiki.summary(values[0], sentences=2)
                wolfram_res = next(client.query(values[0]).results).text
                sg.PopupNonBlocking("Wolfram Result: ", wolfram_res, "Wikipedia Result: ", wiki_res)
            except wiki.exceptions.DisambiguationError:
                wolfram_res = next(client.query(values[0]).results).text
                sg.PopupNonBlocking("Wolfram Result: ", wolfram_res)
            except wiki.exceptions.PageError:
                wolfram_res = next(client.query(values[0]).results).text
                sg.PopupNonBlocking("Wolfram Result: ", wolfram_res)
            except:
                wiki_res = wiki.summary(values[0], sentences=2)
                sg.PopupNonBlocking("Wikipedia Result: ", wiki_res)

            print(values[0])

        window.close()
    except:
        main()

def clear():
    _ = system('clear')
    main()

def randomwiki():
    while True:
        #Getting Wiki's random URL page and finding the title
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

def main():
    print()
    print("Terminal commands: clear")
    print("BRANCH ACCSESS: text; randomwiki")
    while True:
        i = input("branch: ")
        if i == "text":
            text()
        elif i == "clear":
            clear()
        elif i == 'randomwiki':
            randomwiki()
        else:
            print('!error! ~ !retry!')

main()
# This is pretty neat :D Ali Alshawabkeh
