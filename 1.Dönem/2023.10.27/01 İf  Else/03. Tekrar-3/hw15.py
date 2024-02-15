nereye = input('Tiyatromu yoksa sinemsmı\n hepsini küçük yazınız\n')
nesin = input('Tam mı öğrenci mi \n hepsini küçük yazınız\n')

if nereye == ('sinema') and nesin == ('tam'):
    print('15 tl ödiceksin')

elif nereye == ('sinema') and nesin == ('öğrenci'):
    print('7.5 tl ödiceksin')

elif nereye == ('tiyatro') and nesin == ('tam'):
    print('10 tl öde')

elif nereye == ('tiyatro') and nesin == ('öğrenci'):
    print('5 tl öde')