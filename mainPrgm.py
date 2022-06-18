import os

def imp():
    print("Hello")

def printdir():
    print(os.listdir("/"))

print(__name__)
if (__name__ == '__main__'):
    printdir()