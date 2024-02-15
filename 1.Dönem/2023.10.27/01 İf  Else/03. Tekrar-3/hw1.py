note1 = int(input("1. notu giriniz"))

note2 = int(input("2. notu giriniz"))

performance = int(input("performans notunuzu giriniz."))

ghg = (note1 + note2 +performance)/3

if ghg <= 50 :
    print("başarısız")

else :
    print("başarılı")
