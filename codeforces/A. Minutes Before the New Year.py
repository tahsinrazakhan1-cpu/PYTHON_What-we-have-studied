t = int(input())
time = []
for _ in range(t):
    time.append(list(map(int,input().split())))

# print(time)

ans = []
for k in time:
    mins = 0
    min_fromHour = 60*(23 -k[0])
    mins += min_fromHour
    min_fromMinitues = 60 - k[1]
    mins += min_fromMinitues
    ans.append(mins)


for k in ans :
    print(k)