import sys
import codecs
import re
import os

def file_management(file, mode):
    try:
        f = open(file, mode)
        content = f.read()
        return f, content
    except (Exception, TypeError):
        print("wc: " + file + ": No such file or directory")


def wc_c(c, file):
    print(len(c), file)


def wc_m(c, file):
    print(len(c), file)


def wc_l(c, file):
    print(c.count('\n'), file)


def wc_lwm(c, file):
    print(c.count('\n'), len(c.split()), len(c), file)


def wc_L(c, file):
    maxi = max([len(l) for l in c.split('\n')])
    print(maxi, file)


def wc_w(c, file):
    print(len(c.split()), file)


def wc_help():
    try:
        with open("help.txt", "rt") as f:
            print(f.read())
        f.close()
    except:
        print("wc: help: An error occured")


def wc_version():
    print("wc (GNU coreutils) 1.23\nCopyright (C) 2020 Stefan Dragoi, Inc.\n\nWritten by Stefan Dragoi")


def match_wc(cmd):
    regex = re.compile("wc\s(((-c|--bytes|-m|--chars|-l|--lines|-L|--max-line-length|-w|--words)\s.)|--files0-from=\w|--help|--version)")
    return regex.match(cmd)


def wc():
    arguments = sys.argv
    cmd = ' '.join(sys.argv[1:])
    if(not match_wc(cmd)):
        try:
            raise Exception("wc: invalid option -- '" + arguments[2][1:] + "'\nTry 'wc --help' for more information")
        except Exception as e:
            print(e)
    else:
        try:
            if(arguments[2] == '--help'):
                wc_help()
            elif(arguments[2] == '--version'):
                wc_version()
            elif(arguments[2][:14] == '--files0-from='):
                file0 = arguments[2][14:]
                if(os.path.isdir(file0)):
                    try:
                        raise Exception("wc: " + file0 + ": read error: Is a directory")
                    except Exception as e:
                        print(e)
                else:
                    f1, content1 = file_management(file0, "r")
                    if(content1[-3:] != 'txt'):
                        f2, content2 = file_management(content1, "rb")
                        try:
                            content2 = codecs.decode(content2, "utf-8", "ignore")
                        except Exception as e:
                            print(e)
                    else: 
                        f2, content2 = file_management(content1, "r")
                    wc_lwm(content2, content1)
                    f1.close()
                    f2.close()
            elif(os.path.isdir(arguments[3])):
                try:
                    raise Exception("wc: " + arguments[3] + ": Is a directory\n0 wc")
                except Exception as e:
                    print(e)
            elif(arguments[2] == '-c' or arguments[2] == '--bytes'):
                try:
                    f, content = file_management(arguments[3], "rb")
                    wc_c(content, arguments[3])
                    f.close()
                except:
                    pass
            else:
                if(arguments[3][-3:] != 'txt'):
                    f, content = file_management(arguments[3], "rb")
                    try:
                        content = codecs.decode(content, "utf-8", "ignore")
                    except Exception as e:
                        print(e)
                else:
                    f, content = file_management(arguments[3], "rt")
                if(arguments[2] == '-m' or arguments[2] == '--chars'):
                    wc_m(content, arguments[3])
                elif(arguments[2] == '-l' or arguments[2] == '--lines'):
                    wc_l(content, arguments[3])
                elif(arguments[2] == '-L' or arguments[2] == '--max-line-length'):
                    wc_L(content, arguments[3])
                elif(arguments[2] == '-w' or arguments[2] == '--words'):
                    wc_w(content, arguments[3])
                f.close()
        except:
            pass
    

if __name__ == "__main__":
    wc()
    