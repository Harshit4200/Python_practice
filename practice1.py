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
n=int(input("enter the number whose table you want  to print"))
for i in range(1,n):
    for j in range(1,n):
        if(j<n-i):
            print(" ",end="")
        else:
            print("*",end="")
    
    print("\n")
# num=int(input("enter the number whose table you want  to print"))
# for i in range(10,1,-1):
#     print(f"{num}*{i}={num*i}")