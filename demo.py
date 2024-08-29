# num1 = 12 #1100
# num2 = 4  #0100
#and #0100
#or #1100
#xor #1000
#

# print(num1 & num2)
# print(num1 | num2)
# print(~num1)
# print(num1 ^ num2)
# print(num1 >> 2)
# print(num2 >> 3)
# print(num2 << 2)

# def isEvenOdd(n):
#     if(n^1 == n+1):
#         return True;
#     else:
#         return False;

# number = int(input("Enter a number : "))
# if isEvenOdd(number):
#     print(number, "is even")
# else:
#     print(number, "is odd")

def isEvenOdd(n):
    if(n&1 == 1):
        return False
    else:
        return True

number = int(input("Enter a number : "))
if isEvenOdd(number):
    print(number, "is even")
else:
   print(number, "is odd")