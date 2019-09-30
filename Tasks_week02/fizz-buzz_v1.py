#Задача fizz-buzz:
#У вас есть три числа, они вводятся из консоли. Первое число называется fizz, второе называется buzz. До третьего необходимо досчитать от единицы. Считая, надо выводить число. Если число кратно fizz - надо выводить F вместо числа. Если число кратно buzz - надо выводить B вместо числа. Если число кратно и fizz и buzz, надо выводить FB. И так - пока не будет достигнуто третье введенное число.
#Пример условия и результата:
# Введены числа 2, 5, 18
# Вывод должен быть таким:
# 1 F 3 F B F 7 F 9 FB 11 F 13 F B F 17 F
fizz = int(input('Введите число fizz.\n'))
buzz = int(input('Введите число buzz.\n'))
tretie = int(input('Введите третье число.\n'))
print('Выводим последовательность:')
i = 0
vyvod = 0
results = []

for i in range(1,tretie+1,1):
  if i%fizz == i%buzz == 0:
    vyvod = 'FB'
    results += vyvod
  elif i%fizz == 0:
    vyvod = 'F'
    results += vyvod
  elif i%buzz == 0:
    vyvod = 'B'
    results += vyvod
  else:
    vyvod = i
    results += str(vyvod)
print(results)

# for i in range(1,tretie+1,1):
#   if i%fizz == i%buzz == 0:
#     vyvod = 'FB'
#     results.append(vyvod)
#   elif i%fizz == 0:
#     vyvod = 'F'
#     results.append(vyvod)
#   elif i%buzz == 0:
#     vyvod = 'B'
#     results.append(vyvod)
#   else:
#     vyvod = i
#     results.append(vyvod)
# print(results)
# for i in range(1,tretie+1,1):
#   if i%fizz == i%buzz == 0:
#     print('FB')
#   elif i%fizz == 0:
#     print('F')
#   elif i%buzz == 0:
#     print('B')
#   else:
#     print(i)