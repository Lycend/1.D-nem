def üçgen ():
    açı1 = int(input("Açı gir"))  
    açı2 = int(input("Açı gir"))
    açı3 = int(input("Açı gir"))
    toplam = açı1+açı2+açı3
    if toplam == 180:
        print("Üçgen")
    else:
        print("Üçgen Değildir")

üçgen()