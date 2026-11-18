# # # # # # # a = int(input("enter a number "))
# # # # # # # if a % 2 == 0 :
# # # # # # #     print("even no ")
# # # # # # # if a%2!=0:
# # # # # # #     print("odd no")

# # # # # # b = int (input("enter a number "))
# # # # # # if b%3 == 0:
# # # # # #     print("fizz", end = " ")
# # # # # # if b%5 == 0 :
# # # # # #     print("buzz")
# # # # # # # if (b%5==0) and (b%3==0):
# # # # # # #     print("")

# # # # # x = int (input("enter a number "))
# # # # # if 20> x >10 :
# # # # #     x = x +15
# # # # # if   x > 20:
# # # # #     x = x +25

# # # # # print(x)


# # # # marks  = int(input())
# # # # if marks >90 :
# # # #     print("A")
# # # # elif  marks > 80 :
# # # #     print("B")
# # # # elif marks > 70 :
# # # #     print("C")
# # # # elif marks > 60 :
# # # #     print("D")
# # # # elif marks > 50 :
# # # #     print("E")


# # # x = int(input())
# # # if x > 15 :
# # #     if x%6 == 0 :
# # #         print("grt then 15 and divisible then 6")

# # x = int(input())
# # if (x>18):
# #     print("you can vote ")
# # else :
# #     print("you cant vote")

# x = int(input("year no"))
# if x % 4 == 0 or x%100==0 or x%400==0 :
#     print("this is a leap year")
# else:
#     print("this is not A LEAP YEAR ")


# x = int(input())
# if x <= 100 :
#     print(f"Bill: Rs. {x*1.50}")
# elif x>100:
#         print(f"Bill: Rs. {x*2.50}")

x = int(input())
if x % 400 == 0 or x % 4 == 0 and x % 100 != 0:
    print("leap year")
else:
    print(" Not Leap Year")
