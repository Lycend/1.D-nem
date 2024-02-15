def cm():
    return int(input('Boyunuzu Cm olarak giriniz\n'))

def cm_controll(cm):
    if cm < 120:
        print('Büyü de gel')
        return False
    else:
        print('Girebilirsin')
        return True

def age():
    return int(input('Yasinizi giriniz\n'))

def age_controll(age,cm_cont):
    if cm_cont == True:

       if age < 12:
          print('15 tl')
       elif age >= 12 and age <= 18:
         print('25 tl')
       else:
         print('35')


cm_cont = cm_controll(cm)
cm = cm()

age = age()

age_controll(age,cm_cont)