# # # # # while loops
# # # # i = 1
# # # # while i<=5:
# # # #     print("your noob stupid")
# # # #     break

# # # n = int(input())
# # # i = 1
# # # while i<n:
# # #     print("proceccing.")
# # #     print("proceccing..")
# # #     print("proceccing...")
# # #     print("proceccing.")
# # #     print("proceccing..")
# # #     print("proceccing...")
# # #     print("proceccing.")
# # #     print("proceccing..")
# # #     i += 2
# # n = 50
# # while n>0:
# #     print("runs")
# #     n=n//2

# i =0
# while True :
#     print(i)
#     i = i+1
#     # if i == 5:
#     #     break
#     print(i)

i = 1
while True:
    password = input()
    if password == "sesame":
        print("your pass word is correct")
        break
    print("incorrect")
    i += 1
    print("worng PIN", i)
    if i == 5:
        print("you dont have any attept")
