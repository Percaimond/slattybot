import random
import config
import praw
import time
import random as rd
import Slatt

def authenticate():
    reddit = praw.Reddit(
        username=config.username,
        password=config.password,
        client_id=config.client_id,
        client_secret=config.client_secret,
        user_agent=config.user_agent,
    )
    return reddit

def run(reddit):

    for comment in reddit.subreddit(
        "youngthug"
    ).stream.comments(skip_existing=True):
        if (
            "!slattinesebot" in comment.body.lower()
            or "u/slattinesebot" in comment.body.lower()
            and comment.author != "slattinesebot"
            and not comment.saved
        ):
            try:

                msg = "*Beep Boop! I'm a bot! Please contact"
                print("Called")
                parent = comment.parent()
                parBod = parent.body
                with open("test.txt", "r") as cstr:

                    if "!slattinesebot" not in parBod:

                        Slatt.translate(parBod)
                        SlattStr = cstr.read()
                        comment.save()
                        comment.reply(
                            SlattStr + "\n\n" + msg
                        )
                        print("Replied")

            except Exception as e:
                print(e)
                time.sleep(30)

    time.sleep(60)