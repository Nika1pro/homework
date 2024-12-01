numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
simple = []
for num in numbers:
    for i in range(2, num + 1):
        for k in simple:
            if i % k == 0:
                break
        else:
            simple.append(i)
print(simple)

not_simple = []
for i in numbers:
    if not i in simple and i != 1:
        not_simple.append(i)
print(not_simple)

