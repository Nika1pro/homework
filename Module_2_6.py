
n = int(input("Введите число от 3 до 20: "))
if n <= 2:
    print("Попробуйте еще раз. Введите число от 3 до 20")
elif n >= 20:
    print("Попробуйте еще раз. Введите число от 3 до 20")
print()
for i in range(n+1):
    num = " "
    for j in range(1, i):
        for k in range(j + 1, i ):
            if i % (j + k) == 0 and i < 21 and i > 2:
               num += str(j) + str(k)
if i < 21 and i > 2:
    print(i, "-", num)



