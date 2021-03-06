# backend ONLY support for edith.

# Import line
from os import system
import time
import sys
from flask import Flask, render_template, request, flash
# CLASSES tts, ggs, wolframAi, edithGUI, color, and Memory, Config
from EdithOBJs import *
from edithMemory import Memory
from config import config

# config data
config = config()

#flash webserver and resources for messaging
app = Flask(__name__)
app.config['SECERT KEY'] = '8f7403b032a2821e7a10349ae36d158e3d8ccbbfca43fa32'
messages = []

def cq(input):
    remove = lambda v, r: v.replace(r, "")

    a1 = remove(input, "[")
    a2 = remove(a1, "]")
    a3 = remove(a2, "'")
    a4 = remove(a3, ",")
    return a4


def get_answer(q):
    """i/o for edith messages

    Args:
        q (str): input

    Returns:
        str: output
    """        
    q_split = q.split(" ")

    if q_split[0] == "go":
        m = Memory()
        m.acs(str(q))
        return "Done"
    elif q_split[0] in ["answer", "a"]:
        return ggs.answer_search(q)

    elif q_split[0] in ["description", "d"]:
        return ggs.disc_search(q)

    elif q_split[0] == "wolf":
        q_split.pop(0)
        result = cq(str(q_split))

        return wolframAi(result)


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        content = request.form['content']

        if not content:
            flash('Content is required!')
        elif content == "clear":
            messages.clear()
        else:
            messages.clear()
            messages.append(content)
    
            remove = lambda v, r: v.replace(r, "")

            a1 = remove(str(messages), "[")
            a2 = remove(a1, "]")
            a3 = remove(a2, "'")
            fitted = remove(a3, ",")
            answer = get_answer(fitted)
            print(f'the answer is: {answer}')
            full = """
            {% extends 'base.html' %}

{% block content %}
    <h1>{% block title %} Ask ΣA {% endblock %}</h1>
    <form method="post">
        <br>

        <label for="content">Message Content</label>
        <br>
        <textarea name="content"
                  placeholder="Message content"
                  rows="15"
                  cols="60"
                  >{{ request.form['content'] }}</textarea>
        <br>
        <button type="submit">Submit</button>
    </form>
    <br>
    <h3>     
""" + f'Response: \n{answer}' + """ 
    </h3>
{% endblock %}
            """
            f = open("Templates/index.html", "w")
            f.write(full)
            f.close()
            print(f'New Submission Message: {fitted}')
            messages.clear()
    return render_template('index.html')

# clears space
def clear():
    _ = system("clear")
    main()




def get_query():
    """a function that returns IF arguments/flags  was typed to run program.
    e.g. edith wolf 2+2. The function returns wolf 2+2

    Returns:
        a4-str: final query OR
        False-bool: returns False if there is no query
    """
    try:
        sys.argv.pop(0)
        arguments = str(sys.argv)

        if cq(arguments) == '':
            return False
        else:
            return cq(arguments)
        
         
    except:
        return False


def exit():
    _ = system("clear")
    sys.exit()


def exit_no_clear():
    sys.exit()


def start(q):
    # starting init
    if q == False:
        for x in range(20):
            print(color.FAIL + "#")
            time.sleep(0.001)
        for x in range(50):
            print(color.OKCYAN + "#")
        for x in range(30):
            time.sleep(0.004)
            print(color.OKGREEN + "#")
            time.sleep(0.005)
    print(
        color.NORM
        + """
    Ali   Alshawabkeh
    █▀▀ █▀▄ █ ▀█▀ █ █
    ██▄ █▄▀ █  █  █▀█
    ~~~~~~~~~~~~~~~~~
    |███████████▄▄.           |█████| 
    |█|                   |████|   |███|             
     '▀█|                |█|    |██▀' '▀██|               
      '▀█|             |█|    |█'       '▀██|            
       '▀█|                 |█'           '▀██|        
        '▀█|               |█'             '▀██|      
         .▄█|              |█'              '▀██|    
        .▄█|               |████████████████████|  
       .▄█|               |█▀'                '█| 
      .▄█|               |█▀'                  '▀█|     
     .▄█|               |█▀'                     '▀█|      
    .▄█|               |█▀'                        '▀█|    ██▄.
    |███████████▀▀'   |█▀'                           '▀████▀'
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
        + "Abuzz-Industries"
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
        + "1e 1d 91 fe 5d 5e 5d 3c ff d0 2e 8e 1a 23 37 8e f9 8e 43 16 ae e5 60 85 f8 f9 "
        + "1a b8 98 4c c5 5a 43 93 c8 72 09 7e f8 84 96 a1 84 5d 6e 28 8f a7 47 eb 4a 9f "
        + "26 76 ca bd e6 96 87 1f 8d d9 f3 ec"
        + color.NORM
    )


# main loop that runs everything
def main():
    """Main program; loops"""
    if config["config"]["online server"]["host"] == "true": # if using webserver
        print("server starting...")
        if __name__ == '__main__':
            app.run(host='0.0.0.0', port=config["config"]["online server"]["port"], debug=True)
    else: # no websever
        arguments = get_query()
        while True:
            start(arguments)

            if arguments != False:
                q = arguments
            if arguments == False:
                q = input("query: ")
            answer = get_query() 
            if answer != None:
                answer = get_answer(q)
                if q in ['exit', 'ex']:
                    exit()
                else:
                    print(f'Σ̳A̳: {answer}')    
            else:
                print("couldn't get answer? Try again.")
            if arguments != False:
                exit_no_clear()
            else:
                input()
            

main()

# This is pretty neat :D Ali Alshawabkeh
