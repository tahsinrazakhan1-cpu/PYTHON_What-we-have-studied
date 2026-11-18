import weatherdesk

city = input()
temp, rain = weatherdesk.weather_now(city)
baseprice = float(input())
orderlasthour = int(input())
rideronline = int(input())
reason = "No reason"
if temp == -1 or rain == -1:
    print(
        "could not reach sky.... either service is down or city name is not supported"
    )
else:
    pressure = orderlasthour / rideronline if rideronline else float("inf")

    if rain > 0 and pressure > 3:
        surge = 1.5
        reason = "Rain and high demand"
    elif rain > 0:
        surge = 1.3
        reason = "Rain"
    elif temp >= 33 and pressure > 3:
        surge = 1.4
        reason = "High temperature and demand"
    elif temp >= 33:
        surge = 1.2
        reason = "High temperature"
    elif pressure > 4:
        surge = 1.1
        reason = "High demand"
    else:
        surge = 1.0

    final_price = baseprice * surge
    print(final_price)
    print(
        f"Temperature: {temp} C\nRain: {rain} mm\nOrders per rider: {pressure}\nSurge: {surge}\nReason: {reason}\nPrice: {final_price}"
    )
