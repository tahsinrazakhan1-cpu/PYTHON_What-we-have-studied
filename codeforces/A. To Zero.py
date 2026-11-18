t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    x = k - 1
    operations = 0
    while n > 0:
        if n % 2 == 1:
            j = k % x
