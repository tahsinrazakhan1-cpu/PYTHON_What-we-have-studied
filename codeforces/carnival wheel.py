t = int(input())

for _ in range(t):
    l, a, b = map(int, input().split())
    max_prize = a

    for i in range(l):
        position = (a + i * b) % l
        if max_prize < position:
            max_prize = position
    print(max_prize)
