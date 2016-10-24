import time
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
    option= int(raw_input(" [1] Set your own time\n [2] Automatically get Time\n [3] Automatically set time with Date\n USER:"))
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

    else:
        print("Program ending...")
        isRunning = False


