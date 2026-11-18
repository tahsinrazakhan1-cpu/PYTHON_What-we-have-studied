t = int(input())
for _ in range(t):
    name = list(map(str, input().split()))
    country_name = ""
    for i in range(len(name)):
        country_name += name[i][0]
    print(country_name)
