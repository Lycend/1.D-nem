movies = []

def movie_show():
    id = 1
    for movie_key in range(0,len(movies)):
        name = movies[movie_key]['Name']
        director = movies[movie_key]['Director']
        year = movies[movie_key]['Year']
        
        print("\n",id,' =<>= Filmin Adi : ',name,' Yonetmeni : ',director,' Yili : ',year,)
        id += 1



def movie_add():
    movie_name = input('\nFilmin Adi\n')
    movie_director = input('\nFilmin Yazari\n')
    movie_year = int(input('\nFilmin yili\n'))
    movies.append({'Name':movie_name,'Director':movie_director,'Year':movie_year})
    


def movie_delete():
    movie_show()
    movie_key =int(input('\nHangi Filmi Silmek Istiyin\n'))
    movies.pop(movie_key-1)
    print(movie_key,'. Film Silindi')
   
    
    

       

    

    

    



