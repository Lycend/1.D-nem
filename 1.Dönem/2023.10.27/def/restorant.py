menu = {'Ana Yemek':{'Adana':315,'Iskender':520},
           'Salatalar':{'Coban':10,'Tavuk Slatasi':60},
           'Tatlilar':{'Kunefe':300,'Kadayif':200}}

def print_menu():
    for catagory_name in menu.keys():
        print(catagory_name)
        menu_items = menu[catagory_name]
        for meal_name,meal_amount in menu_items:
            print(meal_name,' : ',meal_amount)


def get_orders():   
    while True:
        has_orders = False
        orders = {}
        choose = input('Siparis edeCekmisiniz isterseniz <e> istemezseniz <h>')
        if choose == 'h':
            return has_orders,orders
        
        has_orders == True
        catagory_name = input('Hangi katagoriden alcaksiniz\n')
        if catagory_name not in menu.keys:
            print('Oyle bir kategori yok')

        menu_items = menu[catagory_name]


def print_orders(orders):
    print('Orders i gir')

def has_disconnect(orders):
    return True

def print_disconnect(ordes):
    print('Siparis')

print_menu()

has_order,orders = get_orders()

if has_order:
    print_orders(orders)
 
    if has_disconnect(orders):
        print_disconnect(orders)
else:
    print('Cikildi')