bagaj_kilo = int(input('Hoş geldiniz . Bagaja ne kadar kilo yüklediniz\n'))

if bagaj_kilo <= 20:
    print('Ücretsiz')


else:
    print((bagaj_kilo-20)*10,'TL ödiceksiniz Çünkü',bagaj_kilo-20 , ('Kilo fazla'))
    