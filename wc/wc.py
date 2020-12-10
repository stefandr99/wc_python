import sys
import os
import re

def wc_c(file):
    f = open(file, "rb")
    print(len(f.read()), file)


def wc_m(file):
    f = open(file, "rt")
    print(len(f.read()), file)


def wc_l(file):
    f = open(file, "rt")
    print(f.read().count('\n'), file)


def wc_w(file):
    f = open(file, "rt")
    print(len(f.read().split()), file)


def wc_help():
    with open("help.txt", "rt") as f:
        print(f.read())


def match_wc(cmd):
    regex = re.compile("wc\s(-c|--bytes|-m|--chars|-l|--lines|--files0-from=|-L|-w|--words)\s\w(\\.)\w")
    return regex.match(cmd)


def wc():
    arguments = sys.argv
    cmd = ' '.join(sys.argv[1:])
    if(arguments[2] == '-c' or arguments[2] == '--bytes'):
        wc_c(arguments[3])
    elif(arguments[2] == '-m' or arguments[2] == '--chars'):
        wc_m(arguments[3])
    elif(arguments[2] == '-l' or arguments[2] == '--lines'):
        wc_l(arguments[3])
    elif(arguments[2] == '-w' or arguments[2] == '--words'):
        wc_w(arguments[3])
    elif(arguments[2] == '--help'):
        wc_help()


if __name__ == "__main__":
    wc()
