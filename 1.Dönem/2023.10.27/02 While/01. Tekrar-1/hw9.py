grn_sayı=int(input('Sayı giriniz\n'))
kac_sayı_Grd =0
ortalama = grn_sayı
while  grn_sayı != 1 :
       kac_sayı_Grd += 1    
       grn_sayı=int(input('Sayı giriniz\n'))
       ortalama +=grn_sayı
       print (ortalama)
       if grn_sayı == 1:
         print(ortalama/kac_sayı_Grd)     
         
        