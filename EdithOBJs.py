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
