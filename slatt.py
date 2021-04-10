
import random as rd
import sys

#ip = "All that glitters is not gold By the pricking of my thumbs, Something wicked this way comes.
# Open, locks, Whoever knocks! Hell is empty and all the devils are here."#example text for test purposes
ip = 'That is one small step for a man, one giant leap for mankind.'

slattinese = ["+ SLATT++! ", #1
              "* Slime ", #2
              "** Snake ", #3
              "* No kizzy!!!* ", #4
              "* Big Steppa :) ", #5
              " OH OKAY!!! ", #6
              " SKRRRRRRRT ", #7
              " Udiggwhatimsayin??? ", #8
              " !! ", #9
              " ", #10
              " 🐍🐍🐍", #11 \U0001F40D \U0001F40D \U0001F40D
              " Oh really? ", #12
              " ", #13
              " ", #14
              " ",         #15
              " ON GAWD! "         #16
              " ",         #17
              "   ",         #18
              " ",         #19
              " ",         #20
              " "
              ]#Array with all the different specific slang terms(updated to stay up to date)

def translate(ip):
    op = str(ip.split(' '))
    with open('test.txt', 'w' ,encoding='utf8') as test:
        for word in op:
            x = word.replace(' ', str(rd.choices(slattinese,
            # terms in the array get replaced by their relative weights due to the choice() method
            weights=[7, 7, 2, 8, 1, 3, 2, 4, 5, 3, 4, 4, 5, 5, 5, 7, 5,10,12,6])))

            x = x.replace(']', '').replace('[', '').replace(
                "'", '').replace(',', '')
            print(x, end="", file=test)

translate(ip)