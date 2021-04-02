import random
import config
import praw
import time
import random as rd
import slatt

def authenticate():
    reddit = praw.Reddit(
        username = config.username,
        password = config.password,
        client_id = config.client_id,
        client_secret = config.client_secret,
        user_agent = config.user_agent
    )
    return reddit

def run(reddit):

    for comment in reddit.subreddit("testingground4bots").stream.comments():#monitors all comments in the subreddit
        if (#to add more subreddits concatenate them with "+"
            "!slattbot" in comment.body.lower()
            or "u/slattbot" in comment.body.lower()
            and comment.author != "slattbot"
            and not comment.saved
        ):
            try:

                msg = "*Beep Boop! I'm a bot! Please contact me if problems occur :)*"
                print("Called")
                parent = comment.parent()
                parBod = parent.body
                with open("test.txt", "r" ,encoding='utf8') as cstr:

                    if "!slattbot" not in parBod:

                        slatt.translate(parBod)
                        slattStr = cstr.read()
                        comment.save()
                        comment.reply(
                            slattStr + "\n\n" + msg
                        )
                        print("Replied")

            except Exception as e:
                print(e)
                time.sleep(30)

    time.sleep(60)

