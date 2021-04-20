import random
number=random. randint(1,10)
#guess=int(input ("guess the number"))
#hile number!=guess:
  #  guess=int(input("uff!1try again: guess again"))
#else:
  #  print("congratulation!! you are right")
while True:
    guess= int(input("please enter  the number?"))
    if guess==number:
        print("congratulation")
        break
        print("fail")