# # # # # names = "Python"
# # # # # scores = [95, 87, 92]
# # # # # tags = {"Python", "AI", "Beginner"}
# # # # # # print(names[1])
# # # # # # print(scores[1])
# # # # # # # print(tags[1])
# # # # # # tags = ["A", "B", "C"]
# # # # # # print(tags[1])
# # # # # s = "hello"
# # # # # s[0] = "H"
# # # # # print(s)
# # # # lst = [10, 20, 30]
# # # # lst[0] = 99
# # # # print(lst)
# # # print({1, 2, 2, 3, 3, 3})
# # # print([1, 2, 2, 3, 3, 3])
# # s = {1, 2, 3}
# # # s.add(42)
# # # s.add("hello")
# # # # s.add((10, 20))
# # # s.add([1, 2])
# # # print(s)

# # matrix = [[1, 2, 3],
# # [4, 5, 6],
# # [7, 8, 9]]
# # print(matrix[1][2])
# # print(matrix[0][0])
# # print(matrix[2][1])

# data = [
# ("Alice", {95, 87, 92}),
# ("Bob",
# {78, 85, 90}),
# ]
# print(data[0][0])
# print(data[1][1])
# print(88 in data[0][1])


# Write your reference solution here
VIP = set(input().split())
name = input()

if name in VIP:
    print(f"Total VIPs:{len(VIP)}")
    print("VIP Access Granted")
else:
    print(f"Total VIPs:{len(VIP)}")
    print("Not on the list ")
