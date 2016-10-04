import time
today = time.strftime("%d/%m/%Y")

getTime =  time.strftime("%X")
day = time.strftime("%A")

hour = time.strftime("%I")
hour = int(hour)

print(today+" " + day +" "+ "Current Hour is " + str(hour) + " O'Clock")


#the Following python program uses a time stamp to find what class I am in
monday={7:"free",8:"free",9:"python -KE B016" ,10:"free", 11:"Networking- KA 3016", 12:"free", 1:"Python - KE B023", 2:"free", 3:"Networking - KA - 2008", 4:"Law - KE B023", 5:"Law - KE B023", 6:"free"}
tuesday={7:"free",8:"free",9:"free" ,10:"free", 11:"Microprocessors - lab - KE G003", 12:"Microprocessors - lab - KE G003", 1:"free", 2:"Python - Tutorial - KE B023", 3:"free", 4:"free", 5:"free", 6:"free"}
wednesday={7:"free",8:"ambassador Meeting",9:"free" ,10:"Microprocessors - KA-G025", 11:"Networking - lab - AU1006", 12:"Networking - lab - AU1006", 1:"free", 2:"free", 3:"free", 4:"free", 5:"free", 6:"free"}
thursday = {7:"free",8:"free",9:"free" ,10:"microprocessors", 11:"Sytem Infranstructure - Lab", 12:"free", 1:"free", 2:"python - Lab", 3:"Python - Lab", 4:"free", 5:"free", 6:"free"}
friday={7:"free",8:"free",9:"OS - Lab - KA3005" ,10:"Systems Infranstruture - KE 3008", 11:"Systems Infranstructure - KE 3008", 12:"free", 1:"aw - KE 1008", 2:"OS - KA3021", 3:"OS - KA3021", 4:"free", 5:"free", 6:"free"}

#how to show what class I am supposed to be in
print("According to your Timetable you should be in: \t")

if day == "Monday":
    word = monday[hour]
    print(word)
    print("your next Class is : " + str(monday[hour + 1]))

elif day == "Tuesday":
    word = tuesday[hour]
    print(word)
    print("your next Class is : " + str(tuesday[hour + 1]))



elif day == "Wednesday":
    word = wednesday[hour]
    print(word)
    print("your next Class is : " + str(wednesday[hour + 1]))


elif day == "Thursday":

   word=thursday[hour]
   print(word)
   print("your next Class is : " + str(thursday[hour + 1]))


elif day == "Friday":
    word = friday[hour]
    print(word)
    print("your next Class is : " + str(friday[hour + 1]))


else:
    print("No College Classes!!")

input = raw_input("press enter to end.....")

