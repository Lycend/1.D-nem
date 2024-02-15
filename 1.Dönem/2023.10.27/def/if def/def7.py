def keyboard_input():
    return input('Islem Yap')
def keyboard_controll(keyboard):
    add = 1
    while True:
       if keyboard == '1':
           add += 1
           print('Dogru',add,' kerede yaptniz')
           break
       else:
           add += 1
           keyboard

 
keyboard = keyboard_input()
      
keyboard_controll(keyboard)