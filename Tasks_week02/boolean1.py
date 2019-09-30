a1 = int(input('Введите первое число\n'))
st1 = int(input('Введите степень для первого числа\n'))
a2 = int(input('Введите второе число\n'))
st2 = int(input('Введите степень для второго числа\n'))
ast1 = a1**st1
ast2 = a2**st2
print('Result ',ast1,ast2)
if ast1%2 != 0 and ast2%2 != 0:
  print('All numbers are odd')
elif ast1%2 == 0 and ast2%2 == 0:
  print('All numbers are even')
elif ast1%2 == 0 or ast2%2 == 0:
  print('At least one number is even')
else:
  print('At least one number is odd')
b = False
c = False
d = False
if ast1>ast2:
  b = True
elif ast1==ast2:
  c = True
else:
  d = True

if b == True:
  print(ast1,' > ',ast2)
elif c == True:
  print(ast1,' = ',ast2)
else:
  print(ast1,' < ',ast2)
#проверка истинности аргумента, краткая форма записи
if d:
  print(d)
if b:
  print(b)
else:
  print(c)