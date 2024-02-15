kilo = int(input("kilonuzu giriniz "))
boy = float(input("boyunuzu giriniz"))

vki = kilo/(boy*boy)

if vki >18 and vki <25 :
    print("normal")

elif vki >25 and vki <30 :
    print("kilolu")

elif  vki >= 30 and vki <35   :  
    print("obez")

elif vki >= 35 :
    print("ciddi obezzsin ")