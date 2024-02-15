liste=['35', '26', '81', '64']
liste1 = liste.copy()
liste.sort()
liste.reverse()
print(liste)

liste1.reverse()
print(liste1)

liste1.count('26')
print(liste1.count('26'))

liste.remove('81')
print(liste)


liste1.reverse()
liste1.index('64')
print(liste1.index('64'))

liste1.append('1,4')
liste1.append('6,8')

print(liste1)