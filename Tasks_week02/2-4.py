#Ввести число, вывести его разряды и их множители.
a = int(input('Введите любое целое число.\n'))
razryad = int(input('Введите основание разряда:\n'))
print('Определяем разрядность\n')
i = 0
r = razryad**i

while a >= razryad**i:
  r = razryad**i
  print('Степень: ',i,',',razryad,'^',i,' = ',r)
  i += 1
razr_nost = i - 1
chislo = []
print('Разрядность ',razr_nost,'\nЗаписываем число\n')
mnozhitel = a//razryad**razr_nost
ostatok = a - mnozhitel*razryad**razr_nost
print('По ',razr_nost,'разряду множитель ',mnozhitel,'остаток ',ostatok,': ',razryad**razr_nost*mnozhitel,' = (',razryad,'^',razr_nost,')*',mnozhitel)

for razr_nost in range(razr_nost-1,-1,-1):
  mnozhitel = ostatok//razryad**razr_nost
  ostatok = ostatok - mnozhitel*razryad**razr_nost
  print('По ',razr_nost,'разряду множитель ',mnozhitel,'остаток ',ostatok,': ',razryad**razr_nost*mnozhitel,' = (',razryad,'^',razr_nost,')*',mnozhitel)