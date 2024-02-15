kenar1 = int(input('1. kenar uzunluğunu giriniz\n'))

kenar2 = int(input('2. kenar uzunluğunu giriniz\n'))

kenar3 = int(input('3. kenar uzunluğunu giriniz\n'))

if kenar1 == kenar2 == kenar3:
 print('Eşkenar')
elif kenar3 == kenar1 or kenar3 == kenar3:
  print('İkizkenar')

else:
  print('Çeşitkenar')