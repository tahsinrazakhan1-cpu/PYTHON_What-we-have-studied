# n = int(input())

# q1

# i = 0
# while i <= n :
#     j = 1
#     while j <= i :
# if j== i:
# print(j)
# break
#         print(j, end = " ")
#         j += 1
#     print()
#     i += 1

# # q2

# n = int(input())
# i = 1
# while i <= n :
#     j = 1
#     while j <= n-i :
#         print(" ", end = " ")
#         j += 1
#     j = 1
#     while j <= i :
#         print(j,end = " ")
#         j += 1
#     print()
#     i += 1

# # q3

# n = int(input())
# i = 1
# while i <= n :
#     j = 1
#     while j <= n-i :
#         print(" ", end = " ")
#         j += 1
#     j = i
#     while j > 0 :
#         print(j,end = " ")
#         j -= 1
#     print()
#     i += 1

# # extra ques
# n = int(input())
# i = 1
# while i <= n :
#     # first n-1 spaces
#     print(" "*(n-i), end = " ")
#     # stars
#     print("*"*(2*i - 1), )
#     i += 1

# q4

n = int(input())
i = 0
while i <= n:
    j = 1
    while j <= n - i:
        print(" ", end=" ")
        j += 1
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    j = i - 1
    while j > 0:
        print(j, end=" ")
        j -= 1
    print()
    i += 1

# q5
