n, m = map(int, input().split())
tv_set = list(map(int, input().split()))

tv_set.sort()

he_earns = []

for j in range(m):
    if tv_set[j] <= 0:
        he_earns.append(tv_set[j])

total = -sum(he_earns)

print(total)
