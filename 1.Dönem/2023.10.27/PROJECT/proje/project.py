week = int(input('Yurtta kac hafta kaldiniz \n'))

week_range  = range(1,week+1)

total = 0

week_timer = 1

for week_live in week_range:
    hours = int(input(str(week_timer)+'. haftada kac saat ders yaptin\n'))
    total += hours
    week_timer += 1

chose = input('Eger Toplamini istyosan <T> Ortalama istiyosan <O> basiniz \n')

if chose == 'T':
    print('Toplaminiz : ',total)

elif chose == 'O':
     print('Ortalamasi : ',total/week)
    
else:
    print('Oyle Bir Islem yok')