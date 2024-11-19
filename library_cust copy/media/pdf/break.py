# s="hello"
# for i in s:
#     if(i=='l'):
#         break
#     print(i)


# s="hello"
# for i in s:
#     if(i=='l'):
#         continue
#     print(i)

# l=[12,13,78,35,26,9,7]
# for i in l:
#     if(i%2==0):
#         pass
#     else:
#         print(i)

# 1) s="Python is a programming language"
# print the  string up to a specific character(including that character).
'''s="Python is a programming language"
ch=input("Enter a character:")
for i in s:
    print(i,end=" ")
    if(i==ch):
        break'''

# 2) print those numbers that are not divisible by 7 and 5 in the range(1500,2700) using continue statement.
'''for i in range(1500,2701):
    if(i%5==0 and i%7==0):
        continue
    print(i)'''

# 3) check whether a number is prime or not
num=int(input("Enter a number:"))
for i in range(2,num):
    if(num%i==0):
        print("Not Prime number")
        break
else:
    print("Prime number")


'''count=0
num=int(input("Enter a number:"))
for i in range(2,num):
    if(num%i==0):
        count=count+1
        break
if(count==0):
    print("Number is prime")
else:
     print("Not prime")'''





