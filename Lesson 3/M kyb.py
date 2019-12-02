# Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой набор
# и в каждом наборе все кубики различны по цвету. Однажды дети заинтересовались, сколько существуют
# цветов таких, что кубики каждого цвета присутствуют в обоих наборах. Для этого они занумеровали все цвета
# случайными числами. На этом их энтузиазм иссяк, поэтому вам предлагается помочь им в оставшейся части.
#
# Номер любого цвета — это целое число в пределах от 0 до 10^9.
#
# Входные данные
# В первой строке входного файла записаны числа N и M — количество кубиков у Ани и Бори соответственно.
# В следующих N строках заданы номера цветов кубиков Ани. В последних M строках номера цветов кубиков Бори.
#
# Выходные данные
# Выведите сначала количество, а затем отсортированные по возрастанию номера цветов таких, что кубики каждого
# цвета есть в обоих наборах, затем количество и отсортированные по возрастанию номера остальных цветов у Ани,
# потом количество и отсортированные по возрастанию номера остальных цветов у Бори.
n, m = (int(i) for i in input().split(' '))
#ann = []
#bora = []
#t_color = []
#for j in range(n):
#    ann.append(int(input()))
#for j in range(m):
#    bora.append(int(input()))
#for i in ann:
#    for j in bora:
#        if i == j:
#            t_color.append(j)
#t_color.sort()
#print(len(t_color))
#print(" ".join(map(str, t_color)))
#for i in t_color:
#    for j in ann:
#        if i == j:
#            ann.remove(j)
#for i in t_color:
#    for j in bora:
#        if i == j:
#            bora.remove(j)
#ann.sort()
#print(len(ann))
#print(" ".join(map(str, ann)))
#bora.sort()
#print(len(bora))
#print(" ".join(map(str, bora)))

A, B = set(), set()
for j in range(n):
    A.add(int(input()))
for j in range(m):
    B.add(int(input()))

a_and_b = sorted(A.intersection(B))
onle_a = sorted(A.difference(B))
onle_b = sorted(B.difference(A))

print(len(a_and_b))
print(*a_and_b)
print(len(onle_a))
print(*onle_a)
print(len(onle_b))
print(*onle_b)

