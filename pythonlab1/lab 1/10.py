#write a python program to convert seconds to day,hour,minutes and seconds
second=int(input("enter the time"))
#into minute
minute= second/60
hour= (second/60)/60
day=(((second/60)/60)/24)
remain_second= second * 60
print(f'{second} sec is equal to {minute} min')
print(f"{second} sec is eual to {hour}")
print(f"{second} sec is equal to {day} day")
print (f" {remain_second} is remain seconds")