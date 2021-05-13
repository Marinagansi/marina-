#Write a Python function that takes a number as a parameter and check the number is prime or not.

def multi3(num):
    if num==1:
        return False
    if num==2:
        return True
    if num>2 and num%2==0:
        return True
    if num>2 and num%2!=0:
        return False

num=int(input("enter the number:"))
print(multi3(num))