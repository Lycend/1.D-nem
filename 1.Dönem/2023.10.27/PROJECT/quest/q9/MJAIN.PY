

movies = {}

def movie_show():
    print(movies)    



def movie_add():
    id = len(movies)+1
    movie_name = input('\nFilmin Adi\n')
    movie_director = input('\nFilmin Yazari\n')
    movie_year = int(input('\nFilmin yili\n'))
    movies[id] = {'Name':movie_name,'Director':movie_director,'Year':movie_year}
    


def movie_delete():
    print(movies)
    movie_key =int(input('\nHangi Filmi Silmek Istiyin\n'))
    movies.pop(movie_key)
    print(movie_key,'. Film Silindi')
    print(movies) 
    





options_show = '1'

options_add = '2'

options_delete = '3'

options_exit = 'S'


def show_menu():
    return input(options_show+' = Gosterme\n'+options_add+' = Ekleme\n'+options_delete+' = Silme\n'+options_exit+' = Cikis\n')



while True:
   menu = show_menu()

   if menu == options_show:
       movie_show()

   elif menu == options_add:
       movie_add()

   elif menu == options_delete:
       movie_delete()

   elif menu == options_exit:
       break

   else:
       print('Yanlsi Tuslama')
       
