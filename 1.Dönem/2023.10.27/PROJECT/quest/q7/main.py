import tofodef

while True:

    menu = tofodef.show_menu()

    if menu == '1':
        print('\n','``'*50,'\n')
        print(tofodef.listt)
        print('\n','``'*50,'\n')
   
    elif menu == '2':
        print('\n','``'*50,'\n')
        add = tofodef.add_input()
        tofodef.add_options(add)
        print('\n','``'*50,'\n')
    
    elif menu =='3':
        print('\n','``'*50,'\n')
        tofodef.finish()

    elif menu == '4':

            print('\n','``'*50,'\n')
            print('Cikiliyo...')
            print('\n','``'*50,'\n')
            break
    
    else:
        print('\n','``'*50,'\n')
        print('\nYanlis Tuslama\n')
        print('\n','``'*50,'\n')

 