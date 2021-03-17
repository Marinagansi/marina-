#you live  4 miles from university. the bus drives at 25mph but spends 2 minutes at each  of the  10 stops  on the way.
#how long  will th bus journey take?  Alternativel you could  run to university,you jog the first mile at 7mph then run
#the next two at 15 mph: before jogging the last 7mph again. will this be quicke or slower than the bus
distance=4
speed1=25
#bus stops at 10 places and spent 2 minutes
stop_T=10*2
time=1/speed1
tem=time*60
total_time=tem+stop_T
print(f"the total time to reach university by bus{total_time}")
#the runs with the speed of 7mph
speed2=7
time1=1/speed2
time_1= time1*60
speed3=15
time2=2/speed3
time_2=time2*60
speed4=7
time3=1/speed4
time_3=time3*60
total_time2=time_1+time_2+time_3
print(f"the total time for walking is {total_time2}")

if total_time2<total_time:
    print("walking is faster reach university")
else:
    print("walking is slower")


