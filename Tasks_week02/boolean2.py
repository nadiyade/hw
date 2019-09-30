longtitude = int(input('Введите долготу, в градусах\n'))
latitude = int(input('Введите широту, в градусах\n'))
south = north = east = west = False
if longtitude > 0:
  east = True
else:
  west = True

if latitude > 0:
  north = True
else:
  south = True

if longtitude == latitude == 0:
  print('Вы находитесь на пересечении Гринвичского меридиана и экватора, в Гвинейском заливе')
elif longtitude == 0 and south == True:
  print('Вы находитесь на нулевом меридиане на юг от экватора')
elif longtitude == 0 and south == False:
  print('Вы находитесь на нулевом меридиане на север от экватора')
elif latitude == 0 and east == False:
  print('Вы находитесь на экваторе в западном полушарии')
elif latitude == 0 and east == True:
  print('Вы находитесь на экваторе в восточном полушарии')
elif south == west == True and abs(longtitude) <= 180 and abs(latitude) <= 90:
  print('Вы находитесь на юг от экватора в западном полушарии')
elif south == west == False and abs(longtitude) <= 180 and abs(latitude) <= 90:
  print('Вы находитесь на север от экватора в восточном полушарии')
elif south == True and west == False and abs(longtitude) <= 180 and abs(latitude) <= 90:
  print('Вы находитесь на юг от экватора в восточном полушарии')
elif south == False and west == True and abs(longtitude) <= 180 and abs(latitude) <= 90:
  print('Вы находитесь на север от экватора в западном полушарии')
else:
  print('Вы в космосе')