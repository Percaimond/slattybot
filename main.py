import praw
import slattBot
import time

reddit = slattBot.authenticate()

while True:
        try:
            slattBot.run(reddit)

        except Exception as e:
            print(e)
            continue

        time.sleep(30)