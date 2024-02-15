bütce = int(input("\n\n Mağazaya Hoşgeldiniz.Bütçenizi giriniz\n\n"))

liste = []
while bütce > 0:
    if bütce > 0:
         print('\n\n\nÜrünlerimiz Aşağıda yazıyor\nEt Reyonu = Sosis 100tl,Tavuk 135tl\nİçecek Reyonu = Su 10tl,Shepers 30tl,Çay 60tl,Süt 30tl\nMeyve Reyonu = İncir 50tl,Ananas 70tl\nAburcubur Reyonu = Cips 20tl,Çikolata 7tl\nBunlardan Hangisini alacaksanız Hepsinin Baş Harfi Bğyğk Olmalı.',"\n Çıkmak İçin Qya basınız\n")
         ne_alcan = str(input("Hangisini alıyon :  "))

    if ne_alcan == ("Sosis") and bütce >= 100:
      ne_alcan = int(100)
      bütce-=ne_alcan
      ne_alcan = str("Sosis")
      liste.append(ne_alcan)
      print("\nbütçeniz : ",bütce,"\n",liste)
      
    elif ne_alcan == ("Tavuk")and bütce >= 135:
        ne_alcan = int(135) 
        bütce-=ne_alcan
        ne_alcan = str("Tavuk")
        liste.append(ne_alcan)
        print("\nbütçeniz : ",bütce,"\n",liste)
       
    elif ne_alcan == ("Su")and bütce >= 10:
        ne_alcan = int(10)
        bütce-=ne_alcan
        ne_alcan = str("Su")
        liste.append(ne_alcan)
        print("\nbütçeniz : ",bütce,"\n",liste)
       
    elif ne_alcan == ("Shepers")and bütce >= 30:
        ne_alcan = int(30)
        bütce-=ne_alcan
        ne_alcan = str("Shepers")
        liste.append(ne_alcan)
        print("\nbütçeniz : ",bütce,"\n",liste)
        
    elif ne_alcan == ("Çay")and bütce >= 60:
        ne_alcan = int(60)
        bütce-=ne_alcan
        ne_alcan = str("Çay")
        liste.append(ne_alcan)
        print("\nbütçeniz : ",bütce,"\n",liste)
    elif ne_alcan == ("İncir")and bütce >= 50:
        ne_alcan = int(50)
        bütce-=ne_alcan
        ne_alcan = str("İncir")
        liste.append(ne_alcan)
        print("\nbütçeniz : ",bütce,"\n",liste)
       
    elif ne_alcan == ("Ananas")and bütce >= 70:
        ne_alcan = int(70)
        bütce-=ne_alcan
        ne_alcan = str("Ananas")
        liste.append(ne_alcan)
        print("\nbütçeniz : ",bütce,"\n",liste)
        
    elif ne_alcan == ("Çikolata")and bütce >= 7:
        ne_alcan = int(7)
        bütce-=ne_alcan
        ne_alcan = str("Çikolata")
        liste.append(ne_alcan)
        print("\nbütçeniz : ",bütce,"\n",liste)
        
    elif ne_alcan == ("Cips")and bütce >= 20:
        ne_alcan = int(20)
        bütce-=ne_alcan
        ne_alcan = str("Cips")
        liste.append(ne_alcan)

    elif bütce == 0:
        print("Uygulamadan Çıklıyor...")
 
    else:
       print("\nÖyle Bir Ürün Yok Yada Yetersiz Bakiye\n")

 