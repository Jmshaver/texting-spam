from typing import Union

from fastapi import FastAPI, BackgroundTasks
from texting import send_message
from creds import PEOPLE
import time
import random
app = FastAPI()

MESSAGES = [" I thought you cared about me. Guess I was wrong.","I don't know what I did to make you ignore me, but it really hurts.","This is really important and I need your help ASAP. Please don't ignore me.","You're the only one who can help me with this because you're so smart. Can you please respond?","I don't ask for much, but I really need you right now. Please.","I guess you're too busy for me these days. I'll just deal with this on my own then.","Remember when we used to be so close and you always had my back? I need that friend right now.","If you don't respond, I don't know what I'll do. I'm feeling really low."
            ]

@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/{person}/{message}")
# def read_item(person: str, message: str):
#     print(person, message)
#     if person.lower() in PEOPLE:
#         send_message(PEOPLE[person.lower()]['number'],PEOPLE[person.lower()]['carrier'], 'PLS Respond to Jay', message )
#         return {"Hello": "World"}
def spam(person):
    for _ in range(1):
        send_message(PEOPLE[person.lower()]['number'],PEOPLE[person.lower()]['carrier'], 'PLS Respond to Jay', random.choice(MESSAGES) )
        time.sleep(10)
    
@app.get("/{person}")
def read_item(person: str, background_tasks: BackgroundTasks):
    print(person)
    if person.lower() in PEOPLE:
        background_tasks.add_task(spam, person)
    return {"Hello": "World"}