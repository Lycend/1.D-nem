menu = {'Ana Yemek':{'Adana':3000,'Sosisli':2500},
        'Salata':{'Tavuk Salatasi':5000,'Gavurdag':2000},
        'Icecek':{'Ayran':3000,'Pepsi':1000},
        'Tatli':{'Kunefe':6000,'Yas Pasta':8000}}
orders = []

total = 0

while True:
      operation = input('Siparis vermek icin <e> cikmak icin <h>\n')
      

      if operation == 'h':
            print('Cikiliyor...')
            break
      elif operation == 'e':
            choose = input('Ana Yemek = 1\nSalata = 2\nIcecek = 3\nTatli = 4\n')
            
            if choose == '1':
                  print('\n',menu['Ana Yemek'],'\n')
                  order = input('Hangi yemegi istionuz')
                  if order == 'Adana':
                        orders.append(menu['Ana Yemek'])
                        
            



            elif choose == '2':
                  print('\n',menu['Salata'],'\n')







            elif choose == '3':
                  print('\n',menu['Icecek'],'\n')




            elif choose == '4':
                  print('\n',menu['Tatli'],'\n')


      

      else:
            print('Yanlis Tuslama\n')