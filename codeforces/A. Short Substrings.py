t = int(input())
b = []
ans = []
for _ in range(t):
    b.append(input())

for i in b :
    a = ""
    b_word = i 
    a += b_word[0:2]
    for k in range(3,len(b_word),2):
        a += b_word[k]
    ans.append(a)

for t in ans:
    print(t)