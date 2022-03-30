# GOOGLE SEARCH LIRBRAIES
import requests
from bs4 import BeautifulSoup


class ggs:
    def answer_search(user_query):
        """
        Google data scraping for answer questions


        Args:
            user_query (str): used for i/o communication
        """
        result = ""

        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57"
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        ni = True
        if user_query != "":
            if ni == True:  # Answer 1
                try:
                    result = soup.find(class_="Z0LcW").get_text()
                    ni = False
                except:
                    pass

            if ni == True:  # Answer 2
                try:
                    result = soup.find(
                        class_="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf"
                    ).get_text()
                    ni = False
                except:
                    pass

            if result == "":
                return "Restate the question"
            else:
                return result

    def disc_search(user_query):
        """Google data scraping for description questions

        Args:
            user_query (str): used for i/o communication
        """
        result = ""

        URL = "https://www.google.co.in/search?q=" + user_query

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57"
        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        ni = True
        if user_query != "":
            if ni == True:  # Description 1
                try:
                    result = soup.find(class_="kno-rdesc").get_text()
                    ni = False
                except:
                    pass
            if ni == True:  # Description 2
                try:
                    result = soup.find(
                        class_="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf"
                    ).get_text()
                    ni = False
                except:
                    pass

            if ni == True:  # Description 3
                try:
                    result = soup.find(class_="LGOjhe").get_text()
                    ni = False
                except:
                    pass
            if result == "":
                return "Restate the question"
            else:
                return result


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


# GOOGLE SEARCH LIRBRAIES
import requests
from bs4 import BeautifulSoup

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


# WOLFRAMAI LIRBRAIES
import wolframalpha as wl
import ssl

# wolframalpha api key and ssl bug fix
client = wl.Client("G8X7XT-LH93TX486J")
ssl._create_default_https_context = ssl._create_unverified_context

# WOLFRAMAI
class wolframAi:
    def run(z):
        """used for wolframalpha API calls

        Args:
            z (str): used for i/o communication
        """
        while True:
            if z == ["exit", "ex"]:
                break
            else:
                try:
                    wolfram_res = next(client.query(z).results).text
                    return wolfram_res
                except:
                    print(
                        "Wolfram can't find anything for this... try again?"
                    )
                    print()
                    break


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

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
