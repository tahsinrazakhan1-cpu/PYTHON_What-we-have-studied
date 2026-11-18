t = int(input())
min_diff = []
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    minu = s[1] - s[0]
    for j in range(n - 1):
        if minu > s[j + 1] - s[j]:
            minu = s[j + 1] - s[j]
    min_diff.append(minu)

for k in range(t):
    print(min_diff[k])
