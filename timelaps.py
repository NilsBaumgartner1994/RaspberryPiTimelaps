import scrollphathd
from scrollphathd.fonts import font5x5

from picamera import PiCamera
from os import system
import time

DISPLAY_BAR = False
BRIGHTNESS = 0.3

def showSecondsOnScrollPhatHD(seconds):
    scrollphathd.clear()
    float_sec = (seconds % 60) / 59.0
    seconds_progress = float_sec * 15
    if DISPLAY_BAR:
        for y in range(15):
            current_pixel = min(seconds_progress, 1)
            scrollphathd.set_pixel(y + 1, 6, current_pixel * BRIGHTNESS)
            seconds_progress -= 1
            if seconds_progress <= 0:
                break
    else:
        scrollphathd.set_pixel(int(seconds_progress), 6, BRIGHTNESS)

    hours = str(int(seconds)/60/60).zfill(2)
    minutes = str(int(seconds)/60%60).zfill(2)
    scrollphathd.write_string(hours+":"+minutes,
        x=0, # Align to the left of the buffer
        y=0, # Align to the top of the buffer
        font=font5x5, # Use the font5x5 font we imported above
        brightness=BRIGHTNESS # Use our global brightness value
    )

    if int(seconds) % 2 == 0:
        scrollphathd.clear_rect(8, 0, 1, 5)

    scrollphathd.show()

def getPrintTimeInSeconds(printTime):
    return int(printTime*60*60)

def startRecording(printTime):

    printTimeInSeconds = getPrintTimeInSeconds(printTime)    
    timeEnd = time.time() + printTimeInSeconds
    totalPictures = 180.0
    sleepTime = printTimeInSeconds/totalPictures

    camera = PiCamera()
    camera.resolution = (640,480)
    camera.vflip = True
    camera.hflip = True

    now = time.time()
    start = time.time()
    pictures = 0
    
    while(now < timeEnd):
        camera.capture('image{0:08d}.jpg'.format(pictures))
        print("Pictures: "+str(pictures)+"/"+str(totalPictures))
        timeNextPic = now+sleepTime
        while(now < timeNextPic):
            showSecondsOnScrollPhatHD(timeEnd-now)
            time.sleep(.1)
            now = time.time()

        pictures = pictures+1
        now = time.time()

    return True

def convertToGif(name):
    system('convert -delay 10 -loop 0 image*.jpg '+str(name)+'.gif')
    return True

def cleanUpImages():
    system('rm *.jpg')
