quest = [{'soru1':'Hangi Renk Trafik Lambasi Ortadadir','secenekler1':['A) Yesil','B) Pembe','C) Sari','D) Kirmizi'],'Dogru_Cevap1':'C'},
         
         {'soru2':'Gunes Sistemindeki En buyuk Gezegen','secenekler2':['A) Venus','B) Jupiter','C) Mars','D) Gunes'],'Dogru_Cevap2':'B'},

         {'soru3':'Ay"ın etrafında dönen uydu nedir?','secenekler3':['A) Gracel ve Gratel','B) Gramel ve Gracel','C) Grail A ve Grail B','D) Somius ve Camius'],'Dogru_Cevap3':'C'},
         
         {'soru4':'DNA"nın tam açılımı nedir?','secenekler4':['A) Deoksiriboza nakledilen asit','B) Deoksiribozun nişastalı asit','C) Dayak yiyen nükleik asit','D) Deoksiriboz nükleik asit'],'Dogru_Cevap4':'D'},

         {'soru5':'Aristoto Pelesin Element Tablosunda Hangi elemetler varidr','secenekler5':['A) Ates Sapan Toprak Hava','B) Ates Su Toprak Hava','C) Ates Su Tahta Hava','D) Ates Su Toprak Tahta'],'Dogru_Cevap5':'B'},
       
]


total_true = 0

print('^'*50)

quest_1 = quest[0]['soru1']

quest_2 = quest[1]['soru2']

quest_3 = quest[2]['soru3']

quest_4 = quest[3]['soru4']

quest_5 = quest[4]['soru5']

options_1 = quest[0]['secenekler1']

options_2 = quest[1]['secenekler2']

options_3 = quest[2]['secenekler3']

options_4 = quest[3]['secenekler4']

options_5 = quest[4]['secenekler5']

print('\n',quest_1,'\n')
print('^'*50,'\n')
print(options_1)
print('\n','^'*50,'\n')

answer = input('Bu Sorun Cevabini Yaziniz\n').lower()

print('\n','^'*50,'\n')

if answer == 'c':
    print('\n','^'*50,'\n')
    print('Dogru Cevap Verdiniz\n')
    print('\n','^'*50,'\n')
    total_true += 1

else:
    print('\n','^'*50,'\n')
    print('Yanlis Cevap Verdiniz\n')
    print('\n','^'*50,'\n')

print('\n',quest_2,'\n')
print('^'*50,'\n')
print(options_2)
print('\n','^'*50,'\n')

answer = input('Bu Sorun Cevabini Yaziniz\n').lower()

if answer == 'b':
    print('\n','^'*50,'\n')
    print('Dogru Cevap Verdiniz\n')
    print('\n','^'*50,'\n')
    total_true += 1

else:
    print('\n','^'*50,'\n')
    print('Yanlis Cevap Verdiniz\n')
    print('\n','^'*50,'\n')

print('\n',quest_3,'\n')
print('^'*50,'\n')
print(options_3)
print('\n','^'*50,'\n')

answer = input('Bu Sorun Cevabini Yaziniz\n').lower()

if answer == 'c':
    print('\n','^'*50,'\n')
    print('Dogru Cevap Verdiniz\n')
    print('\n','^'*50,'\n')
    total_true += 1

else:
    print('\n','^'*50,'\n')
    print('Yanlis Cevap Verdiniz\n')
    print('\n','^'*50,'\n')




print('\n',quest_4,'\n')
print('^'*50,'\n')
print(options_4)
print('\n','^'*50,'\n')

answer = input('Bu Sorun Cevabini Yaziniz\n').lower()

if answer == 'd':
    print('\n','^'*50,'\n')
    print('Dogru Cevap Verdiniz\n')
    print('\n','^'*50,'\n')
    total_true += 1

else:
    print('\n','^'*50,'\n')
    print('Yanlis Cevap Verdiniz\n')
    print('\n','^'*50,'\n')




print('\n',quest_5,'\n')
print('^'*50,'\n')
print(options_5)
print('\n','^'*50,'\n')

answer = input('Bu Sorun Cevabini Yaziniz\n').lower()

if answer == 'b':
    print('\n','^'*50,'\n')
    print('Dogru Cevap Verdiniz\n')
    print('\n','^'*50,'\n')
    total_true += 1

else:
    print('\n','^'*50,'\n')
    print('Yanlis Cevap Verdiniz\n')
    print('\n','^'*50,'\n')

if total_true == 5:
    print('ileri Zeka')

elif total_true == 4:
    print('Normal Zeka')

elif total_true == 3:
     print('Geri Zekali')

elif total_true == 2:
    print('zekasız')

elif total_true == 1:
    print('Beyni Maymunlar Tarafindan Alinmis')

elif total_true == 0:
    print('Beyni Doğmadan Önce gitmiş ')

