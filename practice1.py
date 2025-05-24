import random
# Q1
# num1=int(input("enter first number:"))
# num2=int(input("enter second number:"))
# sum = num1+num2
# print("sum:",sum)
# # Q2
# remainder=num1%num2
# print("remainder:",remainder)
# # Q3
# print((num1+num2)/2)
# # Q4
# square=num2*num2
# print(square)
# Q5
# name=input("enter name:")
# print(name.replace("  "," "))
# Q6
# hintoeng = {
#     "Namaste":"	Hello ",
# 	"Dhanyavaad"	:"Thankyou",
# 	"Kripya":	"Please",
# 	"Kaise ho?" :	'How are you?'
# }
# inp= input ("enter hindi word")
# print(hintoeng.get(inp))
# Q7
# unique = set()
# unique.add(int(input('enter number')))  
# unique.add((input('enter number')))  

# print(unique)
# Q8
# dict={
#     "harshit":"hindi",
#     "harsh":"english",
#     "himesh":"spanish",
#     "harshit":"italian"
# }
# print(dict)
# Q9
# num=int(input("enter num"))
# num1=int(input("enter num"))
# num2=int(input("enter num"))
# num3=int(input("enter num"))
# if(num>num1 and num>num2 and num>num3):
#     print(num)
# elif(num1>num and num1>num2 and num1>num3):
#     print(num1)
# elif(num2>num and num2>num1 and num2>num3):
#     print(num2)
# else:
#     print(num3)
# Q10
# sub1=int(input("enter marks:"))
# sub2=int(input("enter marks:"))
# sub3=int(input("enter marks:"))
# if(((sub1+sub2+sub3)/300)*100>40 and sub1>33 and sub2>33 and sub3>33):
#     print("passed")
# else:
#     print("failed")
# Q11
# spam=["Make a lot of money", "buy now", "subscribe this", "click this"]
# email="click this to get 10000 rupees"
# if (spam[0] in email):
#     print("fraud")
# elif (spam[1] in email):
#     print("fraud")
# elif (spam[2] in email):
#     print("fraud")
# elif (spam[3] in email):
#     print("fraud")
# else:
#     print("valid")
# Q12
# user="harshit"
# if(len(user)<10):
#     print("valid")
# else:
#     print("not valid")
# Q13
# list = ["harsh","harsh","aman","ashish"]
# name = "harsh"
# if(name in list):
#     print("yes")
# else:
#     print("no")
# list = [ 1,24,35,"dfijioc",False]
# i=0
# while i<len(list):
#     print(list[i])
#     i+=1
# for i in range(0,len(list)):
#     print(list[i])
# l = ["Harry", "Soham", "Sachin", "Rahul"] 
# for item in l: 
#     if(item.startswith("S")):
#         print(f"hello, {item}")
# i=1
# num=int(input("enter the number whose table you want  to print"))
# while i<11:
#     print(f"{num}*{i}={num*i}")
#     i+=1
# num=int(input("enter the number whose table you want  to print"))
# isprime=0
# for i in range(2,num-1,1):
#     if(num%i==0):
#         isprime=1
#         print("not prime")
# if(isprime==0):
#     print("is prime")
# i=1
# num=int(input("enter the number whose table you want  to print"))
# sum=0
# while i<num+1:
#     sum+=i
#     i+=1
# print(sum)
# num=int(input("enter the number whose table you want  to print"))
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print(fact)
# n=int(input("enter the number whose table you want  to print"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(j<n-i+1):
#             print(" ",end="")
#         else:
#             print("*",end="")
#     for k in range(1,n+1):
#         if(k<i):
#             print("*",end="")
#     print("\n")
# num=int(input("enter the number whose table you want  to print"))
# for i in range(10,1,-1):
#     print(f"{num}*{i}={num*i}")

# n=int(input("enter the number whose table you want  to print"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==1 or i==n):
#             print("*",end="")
#         elif(not(j==1 or j==n)):
            #  print(" ",end="")
#         else:
#             print("*",end="")
#     print("\n")
# def greatest(n1,n2,n3):
#     if(n1>n2 and n1>n3):
#         return n1
#     if(n2>n1 and n2>n3):
#         return n2
#     if(n3>n2 and n3>n1):
#         return n3

# great=greatest(232,3,53)


# def celtofah(cel):
#     fahrenheit=(cel*1.8)+32
#     return fahrenheit

# print(celtofah(20))

# def sumofn(n):
#     if(n==1):
#         return 1
#     return n+sumofn(n-1)

# print(sumofn(5))

# def inchtocm(inch):
#     return inch*2.54

# print(inchtocm(6))

# def pattern(n):
#     for i in range(n,0,-1):
#         for j in range(i):
#             print("*",end="")
#         print()

# pattern(4)

# f= open("poems.txt","r")
# data=f.read()
# if("twinkle" in data):
#     print("yes")
# else:
#     print("NO")
# f.close()

# def game():
#     return random.randint(1,100)
# score=game()

# with open("hi-score.txt","r+") as file:
#     data = file.read()
#     if data=="":
#         file.write(str(score))
#     else:
#         if(int(data)<=score):
#             file.seek(0)
#             file.write(str(score))
#         else:
#             pass





# for i in range(2,21):
#     f=open(f"13-year-old/table{i}.txt","w")
#     for j in range(1,11):
#         f.write(f"{i}*{j}={i*j}\n")
#     f.close()
    

# with open("don.txt","r+") as f:
#     data=f.read()
#     data =data.lower()
#     f.seek(0)
#     if "donkey" in data:
#         f.write(data.replace("donkey","#####"))
#         f.truncate()
#     else:
#         print("no donkey")
        

# with open("don.txt","r+") as f:
#     data=f.read()
# with open("copy.txt","r+") as f1:
#     data1=f1.read()
# if data==data1:
#     print("both files are identical")
# else:
#     print("not identical")
    
# with open("copy.txt","w") as f:
#     f.truncate()

# import os
# files=os.listdir("/")
# print(files)
# for items in files:
#     if ".log" in items:
#         with open(str(items),"r") as f:
#             data = f.read()
#             if "python" in data:
#                 print("yes")


def isprime(num):
    for i in range(2,num,1):
        if(num%i==0):
            return False
    return True

num=7
print(isprime(num))

def secondmaxunique(listint):
    set1=set(list)
    print(set1)
    secondmax=0
    max=0
    for i in set1:
        if(i>=max):
            secondmax=max
            max=i
    return secondmax



list=[23,34,46,2,343,5,23,2,21,354,688,8584,54,43]
print(secondmaxunique(list))

sentence  = "hi my name is harshit j ddcdvain and i am a developer"
l1=[ i for i in sentence.split(" ") if len(i)>4]
print(l1)

# l2=len([ i for i in sentence.split("") if i in "aeiou"])
# print(l2)


students = {'Alice': 82, 'Bob': 65, 'Charlie': 91, 'David': 73}

for i in students.values():
    sum=+i

avg=sum/len(students)

for i in students.values():
    if i>avg:
        print(students[i])

