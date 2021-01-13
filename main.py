import praw
import SlattineseBot
import time

reddit = SlattineseBot.authenticate()

while True:
    try:
        SlattineseBot.run(reddit)

    except Exception as e:
        print(e)
        continue

    time.sleep(30)