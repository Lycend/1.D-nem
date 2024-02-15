total = 0
def week():
    return  int(input('Yurtta kac hafta kaldiniz \n'))

def week_quest(week_):
    total = 0
    for week in range(1,week_+1):
       hours = int(input(str(week)+'. haftada kac saat ders yaptin\n'))
       total += hours
    return total   
 

def chose():
    return input('Eger Toplamini istyosan <T> Ortalama istiyosan <O> basiniz \n')

def chose_controll(chose_,total):
    if chose_ == 'T': 
       print('Toplaminiz : ',total)
 
    elif chose_ == 'O':
       print('Ortalamasi : ',total/week_)
    
    else:
       print('Oyle Bir Islem yok')
    
week_ = week()

total = week_quest(week_)

chose_ = chose()

chose_controll(chose_,total)

