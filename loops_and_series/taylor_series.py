x = float(input("value of no tylor sires"))
terms = int(input("no of terms"))
n = 1
total = 0
term = 1
while n <= terms:
    total += term
    term *= x / n
    n += 1

print(total)

# # sir method
import maths

x = float(input("value of no tylor sires"))
terms = int(input("no of terms"))
