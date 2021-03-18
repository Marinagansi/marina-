#write a python program to convert seconds to day,hour,minutes and seconds
seconds=int(input("enter the time"))
#into minute
minute= seconds// 60
print(f"{seconds} secis equal to {minute} min")
#into hour
hour= seconds//120
print("hour is", hour)