"""Date class"""

class Date(object):
    day =int(0)
    month = int(0)
    year= int(0)
    def __init__(self, day, month,year):
        #setting the day
        if (day<= 0 and day >= 31):
            print("not a valid day")
        else:
            self.day = int(day)

        if (month <= 0 and month >= 12):
            print("not a valid month")
        else:
            self.month = int(month)

        #setting the year
        if (year <= 1900 and year >= 2020):
            print("not a valid year")
        else:
            self.year = year
       # print("Date created")

    def __str__(self):
        return "{}/{}/{}".format(self.day,self.month,self.year)

