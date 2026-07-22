
# n=5 
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()



# Right angle triangle pattern
# n=5 
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()


# Inverted right angle triangle pattern
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(n-i):
#         print("*",end=" ")
#     print()


# Diamond pattern
# Upper half of the diamond
# n=5                                                                             
# for i in range(n):                                                 
#     for j in range(n-i-1): # 
#         print(" ",end=" ")
#     for k in range(2*i+1): #  9 Star
#         print("*",end=" ")
#     print()

# # Lower half
# for i in range(n - 2, -1, -1):
#     for j in range(n - i - 1):
#         print(" ", end=" ")
#     for k in range(2 * i + 1):
#         print("*", end=" ")
#     print()


# Armstrong Number
# 153 = 1^3 + 5^3 + 3^3
# n = int(input("Enter a number: "))
# sum = 0
# temp = n # 153
# while temp>0: # 
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10
# if sum == n:
#     print(n,"is an Armstrong number")
# else:
#     print(n,"is not an Armstrong number")


# Hollow Square Pattern
# n = 5
# for i in range(n):  
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")



# Pascal numbers
n = 5
for i in range(n):
    num = 1

    # Print leading spaces
    for j in range(n - i):
        print("   ", end="")

    # Print Pascal numbers with spacing
    for j in range(i + 1):
        print(f"{num:3}", end="   ")
        num = num * (i - j) // (j + 1)

    print()