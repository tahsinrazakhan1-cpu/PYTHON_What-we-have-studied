# # # # # l = list(map(int,input().split()))
# # # # # maxi = 0
# # # # # i = 0
# # # # # while i < len(l):
# # # # #     if maxi < l[i]:
# # # # #         maxi = l[i]
# # # # #     i += 1
# # # # # print(maxi)
# # # # l = [3,9,0,204,,-8,-8,100,7,44,56]
# # # # f_max = max(l[0], l[1])
# # # # Smax = max(l[0])
# # # # while i < len - :

# # # i = 1
# # # while i <= 2:
# # #     j = 1
# # #     while j <= 3:
# # #         print(i * j, end=" ")
# # #         j += 1
# # #     print()
# # #     i += 1
# # i = 1
# # while i <= 4:
# #     j = 1
# #     while j <= i:
# #         print(i, end=" ")
# #         j += 1
# #     print()
# #     i += 1

# i = 1
# while i <= 4:
#     j = 1
#     while j <= 4:
#         if (i * j) % 2 == 0:
#             print("E", end=" ")
#         else:
#             print("O", end=" ")
#         j += 1
#     print()
#     i += 1


i = 1
while i <= 2:
    a = 1
    while a <= i:
        b = 1
        while b <= 2:
            print("*", end="")
            b += 1
        a += 1
    print("|", end="")
    c = 1
    while c <= 3:
        print("-", end="")
        c += 1
    print()
    i += 1
