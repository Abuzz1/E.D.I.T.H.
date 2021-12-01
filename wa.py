import wolframalpha as wl
from GoogleSearch import tts
# wolframalpha api key
client = wl.Client("G8X7XT-LH93TX486J")


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
