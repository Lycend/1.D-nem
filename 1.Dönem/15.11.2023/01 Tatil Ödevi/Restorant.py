yemek = {"Pizza : 168","Tavuk şiş : 150"}
salata = {"Makarna salatası : 60","Tavuk salatası : 80","Amerikan salatası: 100"}
tatlı = { "Künefe : 100","Treliçe : 50","Baklava : 90"}

indirim =0
yemekleriniz = []
salatalarınız = []
tatlılarınız = []
toplam_fiyat = 0

while True:
    sipariş = input("Restorana hoş geldiniz Şipariş vermek için\n 1 = Ana yemek\n 2 = Salata \n 3 = Tatlı \n 0 = Çıkış\n")
    if sipariş == "0":
        print(yemekleriniz,salatalarınız,tatlılarınız)
        if indirim <3:
          print("\nToplam tutar : ",toplam_fiyat)
          print("Uygulamadan çıkıldı")
        break
       
    if sipariş == ("1"):
     print(yemek)
     ne_alcan = input("Hangi yemeği istiyosunuz\n")
     kaç_tane = int(input("Kaç tane alıyosunuz\n"))
    if ne_alcan == ("Pizza"):
      indirim += 1
      fiyat = 168*kaç_tane
      toplam_fiyat += fiyat
      yemekleriniz.append(kaç_tane)
      yemekleriniz.append(ne_alcan)
      yemekleriniz.append(fiyat)
      print(yemekleriniz)
    if ne_alcan == ("Tavuk şiş"):
      fiyat = 150*kaç_tane
      indirim += 1
      toplam_fiyat += fiyat
      yemekleriniz.append(kaç_tane)
      yemekleriniz.append(ne_alcan)
      yemekleriniz.append(fiyat)
      print(yemekleriniz)
      if sipariş == ("2"):
         print(salata)
         kaç_tane = int(input("Kaç tane alıyosunuz\n"))
         ne_alcan = input("Hangi salatayı istiyosunuz\n")
      if ne_alcan == ("Makarna salatası"):
        fiyat = 60*kaç_tane
        indirim += 1
        toplam_fiyat += fiyat
        salatalarınız.append(kaç_tane)
        salatalarınız.append(ne_alcan)
        salatalarınız.append(fiyat)
        print(salatalarınız)
      if ne_alcan == ("Tavuk salatası"):
        fiyat = 80*kaç_tane
        indirim += 1
        toplam_fiyat += fiyat
        salatalarınız.append(kaç_tane)
        salatalarınız.append(ne_alcan)
        salatalarınız.append(fiyat)
        print(salatalarınız)
      if ne_alcan == ("Amerikan salatası"):
        fiyat = 100*kaç_tane
        indirim += 1
        toplam_fiyat += fiyat
        salatalarınız.append(kaç_tane)
        salatalarınız.append(ne_alcan)
        salatalarınız.append(fiyat)
        print(salatalarınız)
    if sipariş == ("3"):
     print(tatlı)
     ne_alcan = input("Hangi yemeği istiyosunuz\n")
     kaç_tane = int(input("Kaç tane alıyosunuz\n"))
    if ne_alcan == ("Künefe"):
      fiyat = 100*kaç_tane
      indirim += 1
      toplam_fiyat += fiyat
      tatlılarınız.append(kaç_tane)
      tatlılarınız.append(ne_alcan)
      tatlılarınız.append(fiyat)
      print(tatlılarınız)
    if ne_alcan == ("Baklava"):
      fiyat = 90*kaç_tane
      indirim += 1
      toplam_fiyat += fiyat
      tatlılarınız.append(kaç_tane)
      tatlılarınız.append(ne_alcan)
      tatlılarınız.append(fiyat)
      print(tatlılarınız)
    if ne_alcan == ("Treliçe"):
      fiyat = 50*kaç_tane
      indirim += 1
      toplam_fiyat += fiyat
      tatlılarınız.append(kaç_tane)
      tatlılarınız.append(ne_alcan)
      tatlılarınız.append(fiyat)
      print(tatlılarınız)
else:
      print("Lütfen Kategoriden seçiniz")
