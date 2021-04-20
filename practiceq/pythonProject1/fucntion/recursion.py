# def multi(n):
#     if n==1:
#         return 3
#     else:
#         return 3+ multi(n-1)
# for i in range(1,11):
#     print(multi(i))

def sum(l):
    if len(l)==0:
        return 0
    else:
        return l[0]+sum(l[1:])
lst=[2,3,4,5]
print (sum(lst))