

listt = []


while True:
    print('\n','^'*50,'\n')
    choose = input('1 = Ekleme\n2 = Onaylamak\n3 = Cikis\n')
    print('\n','^'*50,'\n')

    if choose == '1':
        
        add = input('Eklemek Istediginiz seyi yaziniz\n')
        print('\n','^'*50,'\n')
        listt.append({add:False})
        print(listt)
        print('\n','^'*50,'\n')

    elif choose == '2':
        print('\n','^'*50,'\n')
        
        for todo in listt:
            print('\n','^'*50,'\n')
            print(todo)
            print('\n','^'*50,'\n')
            confirm = input('Yaptiysan <c> yapmadiysan <nc>\n \v').lower()
            if confirm == 'c':
                print('\n','^'*50,'\n')
                listt.remove(todo)
                print(listt)
                print('\n','^'*50,'\n')
            elif confirm == 'nc':
                 print('\n','^'*50,'\n')
                 print('O metne ddokunmadikn')
                 print('\n','^'*50,'\n')
            else:
                print('\n','^'*50,'\n')
                print('Oyle Bir islem yok')
                print('\n','^'*50,'\n')
    elif choose == '3':
         print('\n','^'*50,'\n')
         print('Cikiliyo...\n')
         print('\n','^'*50,'\n')
         break
    

    else:
        print('\n','^'*50,'\n')
        print('Yanlis Tuslama\n')
        print('\n','^'*50,'\n')
        
               
           