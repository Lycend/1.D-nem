import movie_engine 

movies = movie_engine.movies

options_show = '1'

options_add = '2'

options_delete = '3'

options_exit = 'S'


def show_menu():
    return input(options_show+' = Gosterme\n'+options_add+' = Ekleme\n'+options_delete+' = Silme\n'+options_exit+' = Cikis\n').upper()



while True:
   menu = show_menu()

   if menu == options_show:
       movie_engine.movie_show()

   elif menu == options_add:
       movie_engine.movie_add()

   elif menu == options_delete:
       movie_engine.movie_delete()

   elif menu == options_exit:
       break

   else:
       print('Yanlış Tuşlama')
       
