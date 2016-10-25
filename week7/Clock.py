import time
import os
from time import sleep


class Clock(object):
    today = time.strftime("%d/%m/%Y")
    #strftime("%a, %d %b %Y %H:%M:%S")

    hour=''
    min=''
    sec=''
    #constructor
    def __init__(self,hour1,min1,sec1):
        self.hour=hour1
        self.min=min1
        self.sec=sec1

    #toString
    def __str__(self):

        return "{}:{}:{}".format(self.hour,self.min,self.sec)

    #get date method
    def getDate(self):
        return "{}".format(self.today)

#create an instance of the clock

isRunning=True
while(isRunning):
    option= int(raw_input(" [1] Set your own time\n [2] Automatically get Time\n [3] Automatically set time with Date\n [4] Add two Clocks together\n [5] String Representation\n [6] Live Clock\n  USER:"))
    if(option ==1):
        # manually set the clock
        hour=int(raw_input("enter the hour: hh: "))
        min = int(raw_input("enter the minutes: mm: "))
        sec = int(raw_input("enter the seconds: ss: "))
        timeNow = Clock(hour,min,sec)
        print(timeNow)

    elif(option==2):

        # automatically set the clock
        hours = time.strftime("%H")
        min = time.strftime("%M")
        sec = time.strftime("%S")
        timeNow1 = Clock(hours, min, sec)
        print(timeNow1)

    elif (option == 3):

        # automatically set the clock
        hours = time.strftime("%H")
        min = time.strftime("%M")
        sec = time.strftime("%S")
        timeNow = Clock(hours, min, sec)
        print(timeNow)
        print(timeNow.getDate())

        #create time from two clocks
    elif (option == 4):
        hour = int(raw_input("enter the hour: hh: "))
        min = int(raw_input("enter the minutes: mm: "))
        sec = int(raw_input("enter the seconds: ss: "))
        timeNow = Clock(hour, min, sec)
        print(timeNow)
        hours = time.strftime("%H")
        mins = time.strftime("%M")
        secs = time.strftime("%S")
        timeNow1 = Clock(hours, mins, secs)
        print(timeNow1)

        totalHours = int(hour) + int(hours)
        totalMins = int(min) + int(mins)
        totalSecs = int(sec) + int(secs)
        count = 0

        if(totalSecs > 59):

            totalMins += 1
            remainingSecs = totalSecs - 60
            totalSecs = remainingSecs

        if(totalMins > 59):

            totalHours += 1
            remainingMins = totalMins - 60
            totalMins = remainingMins

        if(totalHours > 23):
            totalHours = 0
            remainingHours = totalHours - 24
            totalMins = remainingHours
            count +=1

        # newTime = Clock(totalHours,totalMins,totalSecs)
        # print("new clock: " + str(newTime))

        newTime2 = Clock(totalHours,totalMins,totalSecs)
        print("new clock: " + str(count) + "Days: " + str(newTime2))

    elif(option == 5):
        clockString = raw_input("Enter the time in the following format (HH:MM:SS):  ")
        sections = []
        sections = clockString.split(":")
        stringClock = Clock(sections[0],sections[1],sections[2])
        print(stringClock)

    elif (option == 6):
        while(1):
            hours = time.strftime("%H")
            mins = time.strftime("%M")
            secs = time.strftime("%S")
            timeNow1 = Clock(hours, mins, secs)
            print(timeNow1)
            sleep(1)
            os.system('cls')


    else:
        print("Program ending...")
        isRunning = False


