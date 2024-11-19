# 1)def add():  # function definition
#     num1 = int(input("Enter a number:"))
#     num2 = int(input("Enter a number:")) # function body
#     sum = num1 + num2
#     print("Sum:", sum)
#
# add()  # function call

# 2)define a function to find the factorial of a number
# def fact(n):
#     i=1
#     fact=1
#     while(i<=n):
#       fact=fact*i
#       i=i+1
#     print("factorial", fact)
#
# num = int(input("Enter a number:"))
# fact(num)

# 3)define  a function to reverse a number
# def rev(n):
#     rev=" "
#     for i in range(len(n)-1,-1,-1):
#         rev=rev+n[i]
#     print("Reverse",rev)
#
# num=input("Enter a number:")
# rev(num)

# 4)define a function to check whether a number is prime or not
# def prime(n):
#     for i in range(2, n):
#         if (n % i == 0):
#             print("Not prime")
#             break
#     else:
#         print("Prime")
#
# num = int(input("Enter a number:"))
# prime(num)


# 5)define a function to display a message
# def display(a):
#     print(a)
# s = "python is an interpreted language"
# display(s)

# 6)define a function to check whether a number is armstrong or not
# def arm(n1):
#
#     sum = 0
#     n = len(n1)
#     for i in n1:
#         sum = sum + int(i) ** n
#     if (sum == int(n1)):
#         print("Armstrong")
#     else:
#         print("Not armstrong")
#
# num = input("Enter a number:")
# arm(num)

# function call with arguments

# def add(n1,n2):
#     sum=n1+n2
#     print("Sum:",sum)
#
# num1=int(input("Enter a number:"))
# num2=int(input("Enter a number:"))
# add(num1,num2)

# define a function to calculate simple interest(using arguments)
# simple interest =p*n*r/100 ...
# def interest(p1, n1, r1):
#     simple_interest = p1 * n1 * r1 / 100
#     # print("Simple interest is:", simple_interest)
#     return simple_interest
#
#
# p = int(input("Enter the principle amount:"))
# n = int(input("Enter the number of year:"))
# r = int(input("Enter the rate of interest:"))
# # print(interest(p, n, r))
# si = interest(p, n, r)
# print(si)

# Define a function to check whether a number is zero,positive or negative
# def number(num):
#     if (num > 0):
#         print("Positive number")
#     elif (num < 0):
#         print("Negative number")
#     else:
#         print("Zero")
#
#
# num = int(input("Enter a number:"))
# number(num)
# Define a function to check whether a number is 4 digit,3digit or 2 digit
# def number(num):
#     if (1000 <= num <= 9999):
#         print("4digit number")
#     elif (100 <= num <= 999):
#         print("3digit number")
#     elif (10 <= num <= 90):
#         print("2digit number")
#     else:
#         pass
#
#
# num = int(input("Enter a number:"))
# number(num)

# using return statement
# def number(num):
#     if num > 0:
#         return "Positive number"
#     elif num < 0:
#         return "Negative number"
#     else:
#         "Zero"
#
#
# num = int(input("Enter a number:"))
# print(number(num))

# def number(n):
#     if 1000 <= num <= 9999:
#         return "4digit number"
#     elif 100 <= num <= 999:
#         return "3digit number"
#     elif 10 <= num <= 90:
#         return "2digit number"
#     else:
#         pass
#
#
# num = int(input("Enter a number:"))
# print(number(num))

# def arithmetic_op(n, m):
#     s = n1 + n2
#     d = n1 - n2
#     p = n1 * n2
#     q = n1 / n2
#     return s, d, p, q
#
#
# n1 = int(input("Enter a number:"))
# n2 = int(input("Enter a number:"))
# # result = arithmetic_op(n1, n2)
# # print(result)
# sum,diff,product,quotient=arithmetic_op(n1,n2)
# print(diff)

# define a function to print all prime numbers in the range (1,100) using return statement

# def prime_n():
#     l = []
#     for i in range(1, 100):
#         if i == 1:
#             continue
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             l.append(i)
#     return l
#
#
# print(prime_n())

# def fact():
#     fact=1
#     num=int(input("Enter a number:"))
#     for i in range(1,num+1):
#        fact=fact*i
#     return fact
# print(fact())

# count=int(input("Enter the count:"))
# l=[]
# for i in range(count):
#     e=int(input("Enter the element:"))
#     l.append(e)
#     print(l)

# count=int(input("Enter the count:"))
# s=set()
# for i in range(count):
#     e=int(input("Enter the  element:"))
#     s.add(e)
#     print(s)

# count=int(input("Enter the count:"))
# d={}
# for i in range(count):
#     k=input("Enter the key:")
#     e=input("Enter the  element:")
#     d[k]=e
#     print(d)

# def fun(name,age):
#     print("The name is",name)          #reserved
#     print("The age is",age)
# fun("Arun",23)

# def fun(name,age):
#     print("name is",name)              #keyword
#     print("age is",age)
# fun(age=23,name="Abi")

# def fun(name,age=24):
#     print("Name is:",name)             #default
#     print("Age is:",age)
# fun("Abi")

# def fun(*args):
#     print(sum(args))
#
#
# fun(1, 2, 3, 4, 5)
# fun(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
# def s(*args):
#     sum=0
#     for i in args:
#         print(i)
#         sum=sum+i
#     print(sum)
# s(1,2,3,4,5)

# def fun(*args):
#     print(args)
#
#
# fun(1, 2)
# fun(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# def fun(**kwargs):
#     print(kwargs)
#
#
# fun(a=1, b=2)
# fun(a=1, b=2, c=3, d=4, e=5)
# fun(name='aju', age=21, place='pkd')

# def fun(*args):
#     for i in args:
#      print(i)
#
#
# fun(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# def fun(*args):
#     for i in range(0, len(args)):
#         print(args[i])
#
#
# fun(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# def fun(**kwargs):
#     for i in kwargs:
#         print(i)
#     for i in kwargs.values():
#         print(i)
#     for i, j in kwargs.items():
#         print(i, j)
#
#
# fun(a=1, b=2, c=3)
# fun(name='Anu',age=20,place='pkd')

# def prd(n):
#     product = 1
#     for i in num:
#         product = product * int(i)
#     return product
#
#
# num = input("Enter a number:")
# print(prd(num))
# s="python is a programming language"
# l=s.split()
# l1=[]
# for i in l:
#     l1.append(len(i))
# print(l1)
# a=max(l1)
# print(a,'is the maximum number of word in programming')

# count=0
# l=[1,1,1,2,2,3,4,6,6,7,7,7]
# s=set(l)
# for i in s:
#    print(i,' ',l.count(i))
# # x=0
# # print(x)
# def f():
#     print(x)
# f()
# def f1():
#     global x
#     x=50
#     print(x)
#
#
# def f2():
#     print(x)
# f1()
# f2()

# def outer():
#     x = 20
#
#     def inner():
#         x = 30
#         print("Inside inner function", x)
#
#     print("Inside outer function before calling", x)
#     inner()
#     print("Inside outer function after calling", x)
#
#
# outer()

# import math
# print(math.pi)
# def f1():
#     print(math.pi)
# def f2():
#     print(math.pi)
# f1()
# f2()

# def addition():
#     n1 = int(input("Enter a number"))
#     n2 = int(input("Enter a number:"))
#     add = n1 + n2
#     print(add)
#
#
# def subtraction():
#     n1 = int(input("Enter a number"))
#     n2 = int(input("Enter a number:"))
#     diff = n1 - n2
#     print(diff)
#
#
# def multiplication():
#     n1 = int(input("Enter a number"))
#     n2 = int(input("Enter a number:"))
#     product = n1 * n2
#     print(product)
#
#
# def division():
#     n1 = int(input("Enter a number"))
#     n2 = int(input("Enter a number:"))
#     quotient = n1 / n2
#     print(quotient)
#
# while(1):
#  print("Arithmetic Operation")
#  print("1.Addition")
#  print("2.Subtraction")
#  print("3.Multiplication")
#  print("4.Division")
#  print("5.Exit")
#  op = int(input("Enter your choice:"))
#  if op == 1:
#      addition()
#  elif op == 2:
#      subtraction()
#  elif op == 3:
#      multiplication()
#  elif op == 4:
#      division()
#  elif op == 5:
#      exit()
#  else:
#      print("invalid")
#
#
# def create():
#     count = int(input("Enter the count:"))
#     for i in range(count):
#         e = input("Enter the element:")
#         l.append(e)
#     return l
#
#
# def search(l):
#     e = input("Enter an element to search:")
#     if e in l:
#         print("Element is present")
#     else:
#         print("Element is not present")
#
#
# def display(l):
#     if l:
#         print("List contents:", l)
#     else:
#         print("List is empty")
# l=[]
# while 1:
#     print("List Operations")
#     print("1. Create a list")
#     print("2. Search an element")
#     print("3. Display the list")
#     print("4. Exit")
#     op = int(input("Enter your choice:"))
#
#     if op == 1:
#         l = create()
#     elif op == 2:
#         search(l)
#     elif op == 3:
#         display(l)
#     elif op == 4:
#         exit()
#     else:
#         print("Invalid choice")

# square=lambda x:x**2
# print(square(4))           # lambda function

# def square(x):
#     return x**2            # users-defined function
# print(square(4))

# l1 = [1, 2, 3, 4]
# print(list(map(lambda x: x * x, l1)))

# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x:x%2==0,l)))

# n=[50,22,89,23,5,101,17]
# print(list(filter(lambda x:50<=x<=100,n)))

# n=[23,89,22,56,45,12]
# print(filter(lambda x:x%3==0 and x%5==0,n))

#d={{'name':'Arun','age':23,'place':'ekm'},{'name':'Anu','age':25,'place':'tvm'},{'name':'manu','age':22,'place':'tcr'}}
# def create():
#     count=int(input("Enter the count:"))
#     for i in range(count):
#         k=input("Enter the key:")
#         e=input("Enter the  element:")
#         d[k]=e
#         print(d)
# def search(d):
#     e=input("Enter an element to search:")
#     for i in d:
#         print("Element is present")
#     else:
#         print("Element is not present")
# def display(d):
#     print(d)
# d={}
# while(1):
#     print("Dictionary operation")
#     print('1.Create dictionary')
#     print('2.Search dictionary')
#     print('3.Display dictionary')
#     print('4.Exit')
#     op=int(input("Enter your choice:"))
#     if op==1:
#         d=create()
#     elif op==2:
#         search(d)
#     elif op==3:
#         display(d)
#     elif op==4:
#         exit()
#     else:
#         print("Invalid choice")
# def create():
#     count = int(input("Enter the count:"))
#     for i in range(count):
#         e = int(input("Enter the  element:"))
#         s.add(e)
#         print(s)
# def search(s):
#     e=input("Enter an element to search:")
#     for i in s:
#         print("Present")
#     else:
#         print("Not present")
# def display(s):
#     print(s)
# s=set()
# while(1):
#     print("Set operations")
#     print('1.create a set')
#     print('2.search a set')
#     print('3.display the set')
#     print('4.exit')
#     op=int(input("Enter your choice:"))
#     if op==1:
#         create()
#     elif op==2:
#         search(s)
#     elif op==3:
#         display(s)
#     elif op==4:
#         exit()
#     else:
#         print("Invalid choice")

# n=['pyton','c','java']
# print(list(lambda x:x))
#sum
# n=[1,2,3,4]
# import functools
# print(functools.reduce(lambda x,y:x+y,n))
#product
# import functools
# print(functools.reduce(lambda x,y:x*y,n))

# import math
# l = [81, 64, 25, 16, 100]
# s= list(map(math.sqrt, l))
# print(s)

# l=[23,45,100,102,678,56,34,90]
# print(list(filter(lambda x:x<100,l)))

# s = ['red', 'green', 'yellow', 'blue', 'violet']
# f = list(filter(lambda x: len(x) < 5, s))
# print(f)

# l = [3, 6, -12, -5, -34, 56, -25, 77]
# import functools
#
# o = list(filter(lambda x: x > 0 and x % 2 != 0, l))
# print('sum of positive odd number:',functools.reduce(lambda x, y: x + y, o))
# e = list(filter(lambda x: x > 0 and x % 2 == 0, l))
# print('sum of positive even number:',functools.reduce(lambda x, y: x + y, e))
# o1 = list(filter(lambda x: x < 0 and x % 2 != 0, l))
# print('sum of negative odd number:',functools.reduce(lambda x, y: x + y, o1))
# e1 = list(filter(lambda x: x < 0 and x % 2 == 0, l))
# print('sum of negative even number:',functools.reduce(lambda x, y: x + y, e1))
# n1=list(filter(lambda x:x>0,l))
# n2=list(filter(lambda x:x<0,l))
# print('Count of positive',len(n1))
# print('count of negative',len(n2))


