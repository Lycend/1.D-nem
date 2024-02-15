sayı = int(input("sayı gir\n"))
kac_kere_girdi = 1
toplam = 0

 
while sayı != 1:
      toplam += sayı
      ortalama = toplam/kac_kere_girdi
      kac_kere_girdi += 1
      print(ortalama)
      sayı = int(input("sayı gir\n"))

    