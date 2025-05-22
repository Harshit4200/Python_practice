import math
import random
# class programmer:
#     def __init__(self,name,salary,position):
#         self.name=name
#         self.salary=salary
#         self.position=position
    
#     def print(self):
#         print(f"Hi,My name is {self.name} and my salary is {self.salary} and i am working on {self.position} position in microsoft")
    
# harshit = programmer("harshit",1000000,"HR")
# harshit.print()
# harsh = programmer("harsh",1000500,"BA")
# harsh.print()

# class calculator:
#     @staticmethod
#     def square(num):
#         print(pow(num,2))
    
    
#     @staticmethod
#     def cube(num):
#         print(pow(num,3))
    
#     @staticmethod
#     def sqroot(num):
#         print(math.sqrt(num))
    
    
# a=calculator()
# a.square(2)
# a.cube(3)
# a.sqroot(16)

# class Train:
#     @staticmethod
#     def book_ticket():
#         print("")
#     @staticmethod
#     def get_status():
#         print("")
#     @staticmethod
#     def get_fare():
#         print("")

# class vector2d:
#     pass

# class vector3d(vector2d):
#     pass

# class animals:
#     pass
# class pets(animals):
#     pass
# class dog(pets):
#     @staticmethod
#     def bark():
#         print("wooh woo")

# dog1=dog()
# dog1.bark()

# class complex:
#     def __init__(self,value,value1):
#         self.a=value
#         self.b=value1

#     def __add__(self,other):
#         return complex(self.a+other.a,self.b+other.b) 
    
#     def __sub__(self,other):
#         return complex(self.a-other.a,self.b-other.b) 

#     def __mul__(self,other):
#         return complex(self.a*other.a-self.b*other.b,self.a*other.b+self.b*other.a)
    
#     def __truediv__(self,other):     
#         return complex((self.a*other.a+self.b*other.b)/(pow(other.a,2)+pow(other.b,2)),(self.b*other.a-self.a*other.b)/(pow(other.a,2)+pow(other.b,2)))

#     def __eq__(self, other):
#           if self.a==other.a and other.a==other.b:
#                 print("both are equal")

#     def __str__(self):
#         return f"your number is {self.a}+{self.b}i"

# c1=complex(2,3)
# c2=complex(3,4)
# c3=c1+c2
# c4=c1-c2
# c5=c1*c2
# c6=c1/c2
# print(f"addition:{c3}\nsubtraction:{c4}\nmultiplication:{c5}\ndivision:{c6}")


# class nvector:

#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
    
#     def __add__(self,other):
#         print(f"{self.i+other.i}i+{self.j+other.j}j")

#     def __dot__(self,other):
#         print(f"{self.i*other.i}i+{self.j*other.j}j")

# n=nvector(2,3)
# n1=nvector(4,5)
# n+n1
# n.n1

# GUESS THE NUMBER GAME

# def gen():
#     return random.randint(1,101)

# comp_num = gen()
# num=int(input("Guess the number:"))
# count = 0 
# while (1):
#     count+=1
#     if num==comp_num:
#         print(f"this is your number {num} and you guessed it in {count} no of times")
#         break
#     else:
#         if num<comp_num:
#             print("your guess is lesser than computer number")
#         else :
#             print("your guess is greater than computer number")
#         num=int(input("Guess the number:"))




# class fraction:
#     def __init__(self,num,deno):
        
#         if isinstance(num,float) or isinstance(deno,float):
#             num=str(num)
#             deno=str(deno)
#             len_num=len(num.split(".")[-1])
#             len_deno=len(deno.split(".")[-1])
            
#             max1=pow(10,max(len_num,len_deno))

#             num=int(float(num)*max1)
#             deno=int(float(deno)*max1)

   
#         div= math.gcd(num,deno)
#         self.numerator=num//div
#         self.denominator= deno//div
    
#     @property
#     def denominator(self):
#         return self.deno1
    
#     @property
#     def numerator(self):
#         return self.nume1
    
#     @numerator.setter
#     def numerator(self,value):
#         self.nume1=value

#     @denominator.setter
#     def denominator(self,value):
#         if value!=0:
#             self.deno1=value
#         else:
#             print("denominator cannot be zero")

#     def __add__(self,other):
#         new_deno=self.denominator*other.denominator
#         new_self_nume=self.numerator*other.denominator
#         new_other_nume=other.numerator*self.denominator
#         return fraction(new_self_nume+new_other_nume,new_deno)
    
#     def __sub__(self,other):
#         new_deno=self.denominator*other.denominator
#         new_self_nume=self.numerator*other.denominator
#         new_other_nume=other.numerator*self.denominator
#         return fraction(new_self_nume-new_other_nume,new_deno)
    
#     def __mul__(self,other):
        
#         new_nume=self.numerator*other.numerator
#         new_deno=other.denominator*self.denominator
#         return fraction(new_nume,new_deno)
    
#     def __truediv__(self,other):
        
#         new_nume=self.numerator*other.denominator
#         new_deno=other.numerator*self.denominator
#         return fraction(new_nume,new_deno)
    
#     def __eq__(self,other):
#         if self.numerator== other.numerator and self.denominator== other.denominator:
#             print("both fraction are equal")
#         else:
#             print("both fraction are not equal")

#     def __str__(self):
#         return f"output:{self.numerator}/{self.denominator}"

    
    

# f1= fraction(4,8)
# f2= fraction(4,7)
# f3=f1+f2
# f4=f1-f2
# f5=f1*f2
# f6=f1/f2
# f1==f2
# print(f"{f3}\n{f4}\n{f5}\n{f6}")


class ecart:
    def __init__(self,category,price,quantity,discount):
        self.category = category
        self.price  = price
        self.quantity= quantity
        self.discount = discount

    @property
    def price(self):
        return self.unit_price

    @price.setter
    def price(self,value):
        if value<=0:
            print("please provide positive price")
        else:
            self.unit_price = value



    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self,value):
        if value<=0:
            print("please provide positive price")
        else:
            self._quantity = value




    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self,value):
        if value>=0 and value<=100:
            self._discount = value
        else:
            print("please provide appropriate discount")


    def __add__(self,other):
        if self.category == other.category:
            total_price = ((self.price*self.quantity)+(other.price*other.quantity))
            discount_total_price=total_price-(max(self.discount,other.discount)/100)*total_price
            total_quantity = self.quantity+other.quantity
            return  ecart(self.category,discount_total_price,total_quantity,self.discount)
        else:
            self_total_price =  (self.price*self.quantity) 
            discount_self_total_price=self_total_price-(self.discount/100)*self_total_price
            
            other_total_price =  (other.price*other.quantity) 
            discount_other_total_price=other_total_price-(other.discount/100)*other_total_price

            total_price=self_total_price+other_total_price
            discount_total_price=discount_self_total_price+discount_other_total_price

            total_quantity = self.quantity+other.quantity
            comb_category=self.category+" and "+other.category

            return ecart(comb_category,discount_total_price,total_quantity,other.discount)

    def __mul__(self,value):
        return f"category:{self.category}\nprice:{self.price*value}\nquantity:{self.quantity*value}\ndiscount:{self.discount}"
    
item1 = ecart("shoes",1000,2,10)
item2 = ecart("shoes",3000,1,20)
item3 = ecart("sunglasses",1000,2,15)

item4=item1+item2
item5=item1+item3

print(item4*1)
print(item5*1)
