#given the integer N- the number  of minutes that is passed since midninght
#how many hours and minutes ae displayed on the 24h  digital clock?
#the program should print two numbers: the number of hours (between  0 and 23) and the number of minutes
#(between 0 and 59)
#for example , if N=150, then 150 minutes have passed since midnight - i.e now is 2:30 am. so, the program should print 2:30

N=int(input("enter the number of minutes:"))
hours = (N//60)
minutes= (N%60)
print(f"the hour is {hours}")
print(f"the minutes is {minutes}")
print (f"its {hours}:{minutes} now")