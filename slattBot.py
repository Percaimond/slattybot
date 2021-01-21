import random
import config
import praw
import time
import random as rd
import slatt

def authenticate():
    reddit = praw.Reddit(
        username = '',
        password = '',
        client_id = '',
        client_secret = '',
        user_agent =''
    )
    return reddit

def run(reddit):

    for comment in reddit.subreddit(
        "YoungThug"
    ).stream.comments(skip_existing=True):
        if (
            "!slattBot" in comment.body.lower()
            or "u/slattBot" in comment.body.lower()
            and comment.author != "slattBot"
            and not comment.saved
        ):
            try:

                msg = "*Beep Boop! I'm a bot! Please contact"
                print("Called")
                parent = comment.parent()
                parBod = parent.body
                with open("test.txt", "r") as cstr:

                    if "!slattBot" not in parBod:

                        slatt.translate(parBod)
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

authenticate()