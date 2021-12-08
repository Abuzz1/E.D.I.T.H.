# backend and frontend support for edith.

# Import line
import os
from os import system, name, error
import os.path
import requests
from bs4 import BeautifulSoup
import webbrowser
import time
import sys


# CLASSES tts, ggs, wolframAi, edithGUI, color
from EdithOBJs import *

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
        q = input("Do you want to try wolframAi, search or the speech version? ")
        if q == "search" or q == "sc":
            i = input("answer of descr? ")
            if i == "descr" or i == "d":
                ggs.disc_search()
            elif i == "answer":
                ggs.answer_search()
            else:
                txtVersion()
        elif q == "speech":
            stt.run()
        elif q == "wolframai" or q == "wa" or q == "wolf":
            wolframAi.run()
        elif q == "exit" or q == "ex" or q == "clear":
            clear()
        else:
            print("try again")
            txtVersion()

# gui version
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
        if ans == "y" or "Y":
            url = "https://en.wikipedia.org/wiki/%s" % title
            webbrowser.open(url)
            break
        elif ans == "n" or "N":
            print("Try again!")
            continue
        elif ans == "clear" or "exit" or "ex":
            clear()
        else:
            print("ERROR!")
            print("RETRY!")
            break

# Main run loop to run everything.
def main():
    print(color.NORM +
    """
    █▀▀ █▀▄ █ ▀█▀ █ █
    ██▄ █▄▀ █  █  █▀█
    """
    )

    print(color.NORM+"Welcome to "+color.BOLD+"E.D.I.T.H. "+color.NORM+"("+color.FAIL+"Abuzz-Industies"+color.NORM+")")
    print("Terminal commands: "+color.OKGREEN+"clear"+color.NORM+"; "+color.OKGREEN+"exit"+color.NORM)
    print("BRANCH ACCSESS: "+color.OKGREEN+"assistant"+color.NORM+"; "+color.OKGREEN+"randomwiki"+ color.NORM)


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
