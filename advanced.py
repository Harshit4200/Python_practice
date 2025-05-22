# files=["1.txt","2.txt","3.txt"]
# for item in files:
#     try:
#         with open(item,"r") as f1:
#             f1.read()
#     except Exception :
#         print("file does not exist")

# list = [1,3,5,32,53,6,23,46,46,23,4]

# list1=[]
# for index,item in enumerate(list):
#     if(index==3 or index==5 or index==7):
#         list1.append(item)
#     else:
#         pass
# print(list1)

# num = int(input("enter the number"))
# list=[1,2,3,4,5,6,7,8,9,10]
# list1=[num*i for i in list]
# print(list1)
# with open("tables.txt","w") as file:
#     file.write(str(list1))

# a = int(input("enter the number"))
# b = int(input("enter the number"))
# try:
#     div = a/b
#     print(f"division:{a/b}")
# except ZeroDivisionError:
#     print("INFINITE")

# list =[ 7,14,21,28,35,42,49,56,63,70]
# string=str(list)
# print(string)


# from typing import List, Tuple, Dict, Union 
# def divisible5(num):
#     if(num%5==0):
#         return True
#     else:
#         return False

# lit=[2,53,35,42,34,5,322,2343,200]
# list1 = list(filter(divisible5,lit))
# print(list1)
from functools import reduce
def max1(a,b):
    if(a<b):
        max=b
        return max
    else:
        max=a
        return max
    
lit=[2,53,35,42,34,5,322,2343,200]
print(reduce(max1,lit))