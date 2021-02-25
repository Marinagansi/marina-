#printing formats
name = input("enter your name:")
age = int(input("enter age: "))
print("hello my name is " + name + "and i am " + str(age) + "years old")
print ("helo my name is", name, "and i am", age, "years old")
print ("hello my name is %s and i am %d years old" %(name,age))
print ("helo my name is {} and i am {} yeras old". format(name, age))
print ("hello my name {name} and i am {age} years old")