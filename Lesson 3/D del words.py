# Дана строка, в которой буква h встречается минимум два раза. Удалите из этой строки первое
# и последнее вхождение буквы h, а также все символы, находящиеся между ними.
# In the hole in the ground there lived a hobbit
a = str(input())
s1 = a.find('h')
s2 = a.rfind('h')
print(a[:s1]+a[s2+1::])