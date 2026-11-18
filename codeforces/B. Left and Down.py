# t = int(input())
# # min_cost = []
# for i in range(t):
#     a,b,k = map(int,input().split())
#     gcd = 0
#     w = min(a,b)
#     while w > 0 :
#         if a%w == 0 and b%w == 0 :
#             gcd = w
#         w -= 1
#     dx = a//gcd
#     dy = b//gcd
#     if dx <= k and dy <= k :
#         print(1)
#     else :
#         print(2)


# lets retry

from math import gcd

t = int(input())
for _ in range(t):
    a, b, k = map(int, input().split())
    g = gcd(a, b)
    dx = a // g
    dy = b // g
    if dx <= k and dy <= k:
        print(1)
    else:
        print(2)
