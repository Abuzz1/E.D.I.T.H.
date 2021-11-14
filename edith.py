# backend support for edith.

#Import line
import os
from os import error
from os import system, name
import os.path
import wolframalpha as wl
import wikipedia as wiki
import PySimpleGUI as sg  # SOON TO BE REMOVED
import requests
from bs4 import BeautifulSoup
import webbrowser
import time
import sys

#wolframalpha api key
client = wl.Client("G8X7XT-LH93TX486J")
#Welcome init
print("Welcome")
for x in range(100):
    print("#")
    time.sleep(0.01)
print("Welcome to E.D.I.T.H. (Abuzz-Industies)")

# gui interface
sg.theme("DarkAmber")  # Add a touch of color
# All the stuff inside your window.
layout = [
    [sg.Text("E.D.I.T.H. GUI % Abuzz Industries")],
    [sg.Text("Enter query"), sg.InputText()],
    [sg.Button("Submit")],
]

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
    try:
        # Create the Window
        window = sg.Window("EDITH", layout)
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            try:
                wiki_res = wiki.summary(values[0], sentences=2)
                wolfram_res = next(client.query(values[0]).results).text
                sg.PopupNonBlocking(
                    "Wolfram Result: ", wolfram_res, "Wikipedia Result: ", wiki_res
                )
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
    print("Terminal commands: clear")
    print("BRANCH ACCSESS: assistant; randomwiki")
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
