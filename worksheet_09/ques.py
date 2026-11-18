y = float(input())
if y == 0.0:
    print("No trip.")
elif y <= 2:
    print("Fare: Rs.50.00")
else:
    x = 50 + (15 * (y - 2))
    print(f"Fare: Rs.{x:.2f}", sep="-")
