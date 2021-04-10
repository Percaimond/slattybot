import praw
import slattybot
import time


reddit = slattybot.authenticate()


while True:
        try:
            slattybot.run(reddit)

        except Exception as e:
            print(e)
            continue

        time.sleep(30)