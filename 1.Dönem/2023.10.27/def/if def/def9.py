def lug_input():
    return int(input('Bagaj Kilonuzu Giriiniz\n'))

def lug_controll(lug):
     if lug <= 20:
          print('Ucretiniz : 0 TL')
     else:
         print('UcretiniZ : ',(lug-20)*10,'TL')
    
lug = lug_input()
lug_controll(lug)
