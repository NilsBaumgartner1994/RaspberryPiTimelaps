import sys
import timelaps as tl
import subprocess
import time

def main():
    tl.cleanUpImages()
    name = askForName()
    printTime = askForTime()
    #sub = subprocess.call("./stream.sh &", shell=True)

    if(tl.startRecording(printTime)):
        print "Recorded, now Converting:"
        if(tl.convertToGif(name)):
            print ("Converted, now Cleaning up")
            tl.cleanUpImages()

def askForName():
    return raw_input("Name: ")

def askForTime():
    isNumber = False
    while(not isNumber):
        printTime = raw_input("Print Time: ")
        if(printTime.isdigit()):
            return int(printTime)
        else:
            print "That was not a Number!"
    


if __name__ == '__main__':
    main()
