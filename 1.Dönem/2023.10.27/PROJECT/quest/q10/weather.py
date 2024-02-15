import weather_engine

city = {}

options_show = '1'

options_add = '2'

options_delete = '3'

options_exit = 'Q'



def show_menu():
    return input(options_show + ' = Gosterme\n',options_add+' = Ekleme\n',options_delete+' = Silme\n'+ options_exit+ ' = Cikis')

while True:
    menu = show_menu()