# Для данного числа n<100 закончите фразу “На лугу пасется...” одним из возможных
# продолжений: “n коров”, “n корова”, “n коровы”, правильно склоняя слово “корова”.

n = int(input())
if n % 10 == 1 and n != 11:
    print(n, "korova")
elif (n % 10 == 2 or n % 10 == 3 or n % 10 == 4) and n != 12 and n != 13 and n != 14:
    print(n, "korovy")
else:
    print(n, "korov")