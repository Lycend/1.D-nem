exam1 = int(input('Hoş geldiniz 1. notu giriniz\n'))

exam2 = int(input(' 2. notu giriniz\n'))

performance = int(input('Performans Notunu giriniz \n'))

ortalama = exam1 + exam2 +  performance

if ortalama >= 50:
    print('Başarılı')
else:
    print('Başarısız')