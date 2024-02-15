def user_input():
     return input('Kullanici Adi Girniz')
def passw_input():
     return input('Sifre Adi Girniz')
def login_registry():
    return input('Kayit olmak icin = 1\nGirs Yapmak icin = 2\n')

def all_user():
     all_users = []


def user_pass_true_controll(user_inp,passw_inp):
    if user_inp == 'Turkiye' and passw_inp == '1923':
        print('Giris Basarili')

def user_pass_false_controll(user_inp,passw_inp):
    if user_inp != 'Turkiye' and passw_inp != '1923':
        print('Giris Basarisiz')  

def registry_user(login_res):
    if login_res == '2':
        input('Yeni Kullancic Adi Girniz\n')
def registry_passw(login_res):
    if login_res == '2':
        input('Yeni Sifre Girniz\n')













user_name = user_input()
passww = passw_input()
login_res = login_registry()

user_pass_true_controll(user_name,passww)

user_pass_false_controll(user_name,passww)
