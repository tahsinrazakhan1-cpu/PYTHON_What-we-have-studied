# # x = int(input())
# # y = "Positive"
# # if (x >0 ):
# #     print(y)
# # elif (x>0 and x%2==0):
# #     print("Positive/Even")
# # elif (x>0 and x%2==0 and x > 100):
# #     print("Positive/Even/Large")

# score,attend = map(int,input().split())
# if score>90 :
#     print("Star Student")
# elif attend >90 :
#     print("Perfect Attendence")
# elif  score>90 and attend >90 :
#     print("Star Student + Perfect Attendence")

# Write your reference solution here
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 > num2 and num1 > num3:
    print(num1)
if num2 > num1 and num2 > num3:
    print(num1)
if num3 > num2 and num3 > num1:
    print(num1)
