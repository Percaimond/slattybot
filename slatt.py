
import random as rd
import sys

ip = "All that glitters is not gold By the pricking of my thumbs, Something wicked this way comes. Open, locks, Whoever knocks! Hell is empty and all the devils are here."


slattinese = ["+ SLATT++! ", #1
              "* Slime ", #2
              "** Snake ", #3
              "* No kizzy!!!* ", #4
              "* Big Steppa :) ", #5
              " OH OKAY!!! ", #6
              " SKRRRRRRRT ", #7
              " Udiggwhatimsayin??? ", #8
              " !!", #9
              " ", #10
              " ", #11
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
              ]

def translate(ip):
    op = str(ip.split(' '))
    with open('test.txt', 'w') as test:
        for word in op:

            x = word.replace(' ', str(rd.choices(slattinese,
                                                 weights=[7, 7, 2, 8, 1, 3, 2, 4, 5, 3, 3, 4, 5, 5, 5, 7, 5,10,12,6

                                                          ])))

            x = x.replace(']', '').replace('[', '').replace(
                "'", '').replace(',', '')
            print(x, end="", file=test)



translate(ip)