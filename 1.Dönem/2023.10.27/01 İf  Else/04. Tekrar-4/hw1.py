def sınav ():
    note1 = int(input("not giriniz"))
    note2 = int(input("not giriniz"))
    note3 = int(input("not giriniz"))
    total =(note1+note2+note3)/3
    if total < 50:
        print("Geçemedin")
    else:
        print("Geçtin")

sınav()
