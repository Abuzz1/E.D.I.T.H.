# backend and frontend support for edith.

# Import line
import os
from os import system
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

# clears space
def clear():
    _ = system("clear")
    main()

# Main run loop to run everything.
def start():
    print(color.NORM +
    """
    █▀▀ █▀▄ █ ▀█▀ █ █
    ██▄ █▄▀ █  █  █▀█
    """
    )

    print(color.NORM+"Welcome to "+color.BOLD+"E.D.I.T.H. "+color.NORM+"("+color.FAIL+"Abuzz-Industies"+color.NORM+")")
    print("Terminal commands: "+color.OKGREEN+"clear"+color.NORM+"; "+color.OKGREEN+"exit"+color.NORM)
    print("BRANCH ACCSESS: "+color.OKGREEN+"main()"+color.NORM+"; "+color.OKGREEN+"randomwiki"+ color.NORM)

    #i/o
    while True:
        i = input("branch: ")

        if i == "main()" or i == "as":
            main()
        elif i == "clear":
            clear()
        elif i == "randomwiki":
            randomwiki()
        elif i == "exit" or i == "ex":
            _ = system("clear")
            sys.exit()
        else:
            print("!error! ~ !retry!")

# main loop that runs everything
def main():
    while True:
        q = input("Do you want to try wolframAi, search or the speech version? ")

        if q == "search" or q == "sc":
            i = input("answer of descr? ")
            if i == "descr" or i == "d":
                ggs.disc_search()
            elif i == "answer":
                ggs.answer_search()
            else:
                main()

        elif q == "speech":
            stt.run()

        elif q == "wolframai" or q == "wa" or q == "wolf":
            wolframAi.run()

        elif q == "exit" or q == "ex":
            _ = system("clear")
            sys.exit()
        elif q == "clear":
            clear()

        else:
            print("try again")
            main()
main()
# This is pretty neat :D Ali Alshawabkeh
