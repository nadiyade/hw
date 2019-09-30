#Ввести число, вывести все его делители.
a = ''
a = int(input('Введите любое целое число.\n'))
if a >= 0:
  i = 1
  for i in range(1,a):
    b = a%i
    if b == 0:
      print('Число делится без остатка на ',i)
      i += 1
    else:
      i += 1
else:
  i = -1
  for i in range(a,-1):
    b = a%i
    if b == 0:
      print('Число делится без остатка на ',(-1)*i)
      i -= 1
    else:
      i -= 1  