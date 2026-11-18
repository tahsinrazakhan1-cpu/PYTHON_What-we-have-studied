# first try


# import math
# t = int(input())
# ans = []
# for _ in range(t):
#     n,b = map(int,input().split())
#     new_b = list(map(int,input().split()))
#     fac_2023 = [2023,119,289,17,7]
#     product = math.prod(new_b)
#     exist = False
#     k = 2023//product
#     if  2023%product == 0 :
#         print("Yes")
#         exist = True
#     else :
#         print("No")
#     if exist:
#         if k in fac_2023 :
#             ans.append(k)
#         else :
#             ans.append(1)
#     for j in range(b):
#         if j == b-1 :
#             print(ans[j])
#         else :
#             print(ans[j],end= " ")


# second try
import math

t = int(input())

for _ in range(t):
    n, b = map(int, input().split())
    new_b = list(map(int, input().split()))

    product = math.prod(new_b)

    if 2023 % product == 0:
        print("YES")

        k = 2023 // product
        ans = [k] + [1] * (b - 1)

        print(*ans)
    else:
        print("NO")
