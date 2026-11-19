t = int(input())
abcd = []
for _ in range(t):
    abcd.append(list(map(int,input().split())))

for k in abcd:
    a,b,c,d = k[0],k[1],k[2],k[3]
    e = min(a,b)
    f = max(a,b)
    if e < c < f and (not(e < d < f)):
        print("yes")
    elif e < d < f and (not(e < c < f)):
        print("yes")
    else :
        print("no")