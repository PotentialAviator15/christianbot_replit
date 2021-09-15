from flask import Flask

from threading import Thread



app = Flask('')



@app.route('/')

def home():

    return "I'm online. Thank you for checking the official page of ChristianBot. This version of the bot was released 8/25/2021 "



def run():

  app.run(host='0.0.0.0',port=9080)



def keep_alive():  

    t = Thread(target=run)

    t.start()