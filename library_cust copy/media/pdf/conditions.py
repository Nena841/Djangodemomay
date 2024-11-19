# 1) program to check whether a number is divisible by 7
x = int(input("Enter a number:"))
if(x%7==0):
    print("number is divisible by 7")
else:
    print("number is not divisible by 7")

# 2) program to check whether a number is multiple of 3 and 5
x = int(input("Enter a number:"))
if (x% 3 == 0 & x % 5 == 0):
    print("number is a multiple of 3 and 5")
else:
    print("number is not a multiple of 3 and 5")

# 3) program to check whether an entered character is vowel or not
x=(input("Enter a value:"))
l=['A','E','I','O','U','a','e','i','o','u']
if(x in l):
    print("vowel")
else:
    print("not vowel")

# 4) program to check whether the last digit of a number is divisible by 3 or not
x=int(input("Enter a number:"))
y=x%10
if(y%3==0):
    print("divisible by 3")
else:
    print("not divisible by 3")

# 5) program to check whether the number is a 2-digit number
x=int(input("Enter a number:"))
if(x<=99 & x>=10):
    print("2-digit number")
else:
    print("not 2-digit number")

# 6) program to check whether the two strings are equal or not
x=input("Enter a string:")
y=input("Enter a string:")
if(x==y):
    print("strings are equal")
else:
    print("strings are not equal")

# 7) program to check whether a string is palindrome or not
x=input("Enter a string:")
y=x[::-1]
if(x==y):
    print("palindrome")
else:
    print("not palindrome")

# 8) program to check a number is present in a list or not
x=int(input("Enter a number:"))
l=[1,2,3,4,5]
if(x in l):
    print("number is present")
else:
    print("number is not present")

# 9) program to check a particular key is present in a dictionary or not
x=input("Enter a key:")
d={101: "Abi", 102: "Anu", 103: "Ajin"}
if(x in d):
    print("key is  present")
else:
    print("key is not present")

