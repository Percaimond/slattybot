#!/usr/bin/python3
import random as rd
import sys
#works?
ip = ""

slattinese = [" SLATT++! ", #1
              " Slime", #2
              " 🐍🐍🐍 ", #3
              " No kizzy!!!* ", #4
              " Big Steppa :)", #5
              " OH OKAY!!!+", #6
              " SKRRRRRRRT", #7
              " Udiggwhatimsayin??", #10
              "", #11
              "", #12
              "", #13
              "", #14
              "", #15
              "",
              "",
              "",
              ""]

def translate(ip):
    op = str(ip.split(' '))
    with open('test.txt', 'w') as test:
        for word in op:

            x = word.replace(' ', str(rd.choices(slattinese,
                                                  weights=[4, 5, 2, 2, 3, 3, 2, 4, 5, 3, 3, 4, 5, 5, 8, 7, 5,10,12,6

                                                        ])))

            x = x.replace(']', '').replace('[', '').replace(
                "'", '').replace(',', '').replace(' ', '')
            print(x, end="", file=test)

translate(ip)