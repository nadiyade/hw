#Проверить, является ли введеное число четным.
a = ''
a = int(input('Введите любое целое положительное число.\n'))
if a < 0:
  a = a * (-1)
  print('Введенное число отрицательное, будет применено преобразование: ',a)
else:
  pass

print('\nПроверяем, является ли введеное число четным.')
if a%2 != 0:
  print('Число нечётное, остаток от деления равен ',a%2)
else:
  print('Число чётное, остаток от деления равен ',a%2) 