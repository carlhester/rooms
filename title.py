from __future__ import print_function
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#print "2590", u"\u2590"* 1 
#print "2591", u"\u2591"* 1
#print "2592", u"\u2592"* 1
#print "2593", u"\u2593"* 1 
#print "\n\n"
#
#print u"\u2593" * 30
#print u"\u2593" * 10,
#print u"\u2591" * 10, 
#print u"\u2593" * 10 
#print "\n"
#


def print_title():

    row0 = ".............................."
    row1 = ".xxxx.xxxx.xxxx.x.....x..xxx.."
    row2 = ".x..x.x..x.x..x.xx...xx.x....."
    row3 = ".x..x.x..x.x..x.x.x.x.x..x...."
    row4 = ".xxx..x..x.x..x.x.x.x.x...x..."
    row5 = ".x..x.x..x.x..x.x..x..x...x..."
    row6 = ".x..x.x..x.x..x.x.....x....x.."
    row7 = ".x..x.xxxx.xxxx.x.....x.xxx..."
    row8 = ".............................."

    rows = [row0, row1, row2, row3, row4, row5, row6, row7, row8]


    os.system('clear')

    for each_row in rows:
        for letter in each_row:
            if letter == ".": print(bcolors.OKBLUE + (u"\u2593" * 4) , end='')
            if letter == "x": print(bcolors.FAIL + (u"\u2591" * 4), end='')
        print("\r")

    print(bcolors.ENDC)



