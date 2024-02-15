tek_sayılar =[5,7,9,11,13,15]

cift_sayılar = [6,8,10,12,14,16]
cft = cift_sayılar.copy()
cift_sayılar.extend(tek_sayılar)
cift_sayılar.sort()
print(cift_sayılar)

cift_sayılar.remove(5)
cift_sayılar.remove(6)
cift_sayılar.remove(8)
cift_sayılar.remove(9)
cift_sayılar.remove(10)
cift_sayılar.remove(11)
cift_sayılar.remove(12)
cift_sayılar.remove(13)
cift_sayılar.remove(15)
cift_sayılar.remove(16)
print(cift_sayılar)

print(cft[2],cft[3],'','',tek_sayılar[4])