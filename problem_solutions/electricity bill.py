x = int(input())
if 1 < x <= 100:
    print(f"Bill: Rs.{x * 3:.2f}")
elif 100 < x <= 200:
    print(f"Bill: Rs.{x * 5:.2f}")
elif 200 < x <= 300:
    print(f"Bill: Rs.{x * 7:.2f}")
else:
    print(f"Bill: Rs.{x * 10:.2f}")
