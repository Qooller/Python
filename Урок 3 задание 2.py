a = int(input('Ввдите пятизначное число '))
print('1 цифра равна  {}'.format(a // 10000))
print('2 цифра равна  {}'.format((a // 1000) % 10))
print('3 цифра равна  {}'.format((a // 100) % 10))
print('4 цифра равна  {}'.format((a // 10 % 10)))
print('5 цифра равна  {}'.format((a % 10)))
