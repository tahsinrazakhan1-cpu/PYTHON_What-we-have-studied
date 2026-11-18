n = int(input())
s = list(map(int, input().split()))
s.sort()
min_diff = []
minu = s[1] - s[0]
for j in range(2, n - 1):
    if minu > s[j + 1] - s[j]:
        minu = s[j + 1] - s[j]
    # min_diff.append(minu)

print(minu)
