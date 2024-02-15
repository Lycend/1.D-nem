def product_price_1():
    return int(input('1. Urunun fiyatini girinz \n'))

def product_price_2():
    return int(input('2. Urunun fiyatini girinz \n'))

def product_calculator(product1,product2):
    return (product2+product1)

def product_controll(total):
    if total <=200:
        print(total)
    else:
        print(total-(total/4))
    

product1 = product_price_1()

product2 = product_price_2()

total = product_calculator(product1,product2)

product_con = product_controll(total)
