def weight_ipt():
    return int(input('Agirliginizi giriniz \n'))

def height_ipt():
    return int(input('Boyunuzu giriniz \n'))

def vki_calculator(weight,height):
    return weight/(height*height)

def vki_controll(vki):
     if vki >= 18 and vki <= 25:
         print('Normalsin')
     elif vki >= 25 and vki <= 30:
         print('Kilolu')
     elif vki >= 30 and vki <= 34:
         print('Obez')
     elif vki >= 35 and vki <= 45:
         print('Ciddi Obez')
     elif vki >= 46 and vki <= 55:
        print('Abez')
     elif vki >= 56 and vki <= 70:
        print('Ciddi Abez')
     else:
         print('Emirhan')
    


weight = weight_ipt()
height = height_ipt()
vki = vki_calculator(weight,height)
vki_controll(vki)