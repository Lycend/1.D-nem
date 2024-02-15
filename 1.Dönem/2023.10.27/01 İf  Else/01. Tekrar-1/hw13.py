yıl = int(input('Kaç yıl çalıştınız\n'))

maas = int(input('Maaşınız giriniz\n'))

if yıl >0 and yıl < 6:
    print('Sayın Çalışanımız',maas+(maas/10),'Zamlı Maaşınız')

elif yıl > 5 and yıl < 11:
    print('Sayın Çalışanımız',maas+(maas*(15/100)),'Zamlı Maaşınız')

elif yıl > 11:
    print('Sayın Çalışanımız',maas+(maas*(25/100)),'Zamlı Maaşınız')

