listt = []

def show_menu():
    return input('1 = Gosterme\n2 = Ekleme\n3 = Onaylamak\n4 = Cikis\n')


            
        
        
    
def add_input():
    return input('Eklemek Istediginiz seyi yaziniz\n')

def add_options(add):
    return listt.append({add:'X'})


def finish():
    print(listt)                              
    print('\n','``'*50,'\n')
    
    print('\n','``'*50,'\n')
    if len(listt) <= 0 :
       print('Ilk once Bir Sey ekleyin')
    elif len(listt) > 0:
        item_index = int(input('\nKacinici Gorevi Yaziniz\n'))
        
        
        for todo in listt[item_index-1]:
                if todo == '✓':
                     listt.remove(todo)
                     for print_todo in range(0,len(listt)):
                          print(listt[print_todo])
                else:
                    listt[item_index-1][todo] = '✓'
                    for print_todo in range(0,len(listt)):
                          print(listt[print_todo])

def show_listt():
     for print_todo in range(0,len(listt)):
                          print(listt[print_todo])

    
    
    
while True:

    menu = show_menu()

    if menu == '1':
        print('\n','``'*50,'\n')
        show_listt()
        print('\n','``'*50,'\n')
   
    elif menu == '2':
        print('\n','``'*50,'\n')
        add = add_input()
        add_options(add)
        print('\n','``'*50,'\n')
    
    elif menu =='3':
        print('\n','``'*50,'\n')
        finish()

    elif menu == '4':

            print('\n','``'*50,'\n')
            print('Cikiliyo...')
            print('\n','``'*50,'\n')
            break
    
    else:
        print('\n','``'*50,'\n')
        print('\nYanlis Tuslama\n')
        print('\n','``'*50,'\n')

 
   



   

                        