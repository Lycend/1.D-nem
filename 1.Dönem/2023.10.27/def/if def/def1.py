def note():
    note1 = int(input('Not gir'))
    note2 = int(input('Not gir'))
    note3 = int(input('Not gir'))
    return (note1+note2+note3)/3


if note() < 50:
    print('Kaldiniz')
else :
    print('Gectiniz')