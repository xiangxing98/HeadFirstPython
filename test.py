import sys

if __name__ == "__main__":
    print("hello.")
    for i in range(0, len(sys.argv), 1):
        print("Parameter%d: " % i, sys.argv[i], sep = ' ')
    print("Will Exit.")
    sys.exit(0)
"""
hello.
Parameter0:  e:\Github\Python\HeadFirstPython\HeadFirstPython\test.py
Parameter1:  1st_param
Parameter2:  2nd_param
Will Exit.
"""

