def user_input():
     return input('Kullanici Adi Girniz')
def passw_input():
     return input('Sifre Adi Girniz')


def user_pass_true_controll(user_inp,passw_inp):
    if user_inp == 'Turkiye' and passw_inp == '1923':
        print('Giris Basarili')

def user_pass_false_controll(user_inp,passw_inp):
    if user_inp != 'Turkiye' and passw_inp != '1923':
        print('Giris Basarisiz')  
user_name = user_input()
passww = passw_input()


user_pass_true_controll(user_name,passww)

user_pass_false_controll(user_name,passww)
