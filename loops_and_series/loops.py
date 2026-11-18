# multiply table
x = int(input("of which multiplication table? "))
for i in range(1, 11):
    print(i, "x", x, "=", i * x)

# factors of a number
n = int(input("enter a number to find factors: "))
print("Factors of", n, "are:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

# proper divisors of a number
y = int(input("enter a number to find proper divisors: "))
print("Proper divisors of", y, "are:")
for i in range(1, y // 2 + 1):
    if y % i == 0:
        print(i)
print("Number itself:", y)

# factor pairs using sqrt
import math

t = int(input("enter a number to find factor pairs: "))
print("Factor pairs of", t, "are:")
i = 1
while i <= int(math.sqrt(t)):
    if t % i == 0:
        if i == t // i:
            print(i)
        else:
            print(i, t // i)
    i += 1

# factorial
c = int(input("which factorial do you want? "))
ans = 1
i = 1
while i <= c:
    ans *= i
    i += 1
print(c, "! =", ans)

# prime number check
n = int(input("tell me a number to check if it is prime: "))
if n <= 1:
    print("not prime")
else:
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("prime")
    else:
        print("not prime")
