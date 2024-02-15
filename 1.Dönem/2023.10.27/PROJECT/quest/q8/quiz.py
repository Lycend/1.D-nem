import random

all_quest = [{'Soru':'Dünya üzerinde kaç kıta bulunmaktadır?','secenekler':['A) 4','B) 5','C) 6','D) 7'],'Dogru Cevap':'d'},
             
{'Soru':'Hangi gezegen "Akşam Yıldızı" olarak da adlandırılır?','secenekler':['A) Mars','B) Venüs','C) Jüpiter','D) Satürn'],'Dogru Cevap':'b'},

{'Soru' :'Bir insanın en fazla kaç kalp atışı vardır dakikada?','secenekler':['A) 60','B) 100','C) 120','D) 150'],'Dogru Cevap':'c'},

{'Soru':'Hangi yıl Leonardo da Vinci"nin "Mona Lisa" tablosu çalındı ve 2 yıl sonra geri getirildi?','secenekler':['A) 1972','B) 1986','C) 1994','D) 2003'],'Dogru Cevap':'d'},

{'Soru':'Bir yıl kaç saniyedir?','secenekler':['A)  31,536,000','B) 36,000,000','C) 24,000,000','D) 42,000,000'],'Dogru Cevap':'d'},

{'Soru':'"Romeo ve Juliet" adlı eserin yazarı kimdir?','secenekler':['A) Charles Dickens','B) Jane Austen','C) William Shakespeare','D) Victor Hugo'],'Dogru Cevap':'c'},

{'Soru':'Hangi yıl İstanbul Boğazı" nın suları tuzlu hale gelmiştir?','secenekler':['A) 1923','B) 1936','C) 1945','D) 1957'],'Dogru Cevap':'c'},

{'Soru':'"Süpernova" nedir?','secenekler':['A) Yeni bir gezegen','B) Bir yıldızın patlaması','C) Bir galaksinin çarpışması','D) Bir kara delik'],'Dogru Cevap':'b'},

{'Soru':'Hangi yıl "Twitter" platformu kullanıma açılmıştır?','secenekler':['A) 2004','B) 2006','C) 2008','D) 2010'],'Dogru Cevap':'b'},

{'Soru':'"Dördüncü Duvar" terimi hangi sanat dalında kullanılır?','secenekler':['A) Sinema','B) Tiyatro','C) Resim','D) Müzik'],'Dogru Cevap':'b'},

{'Soru':'Hangi gezegenin uydusu "Titan" üzerinde göl ve nehir sistemleri bulunmaktadır?','secenekler':['A) Mars','B) Jüpiter','C) Satürn','D) Uranüs'],'Dogru Cevap':'c'},

{'Soru':'Hangi yıl ve nerede ilk insan klonlandı?','secenekler':['A) 1997, ABD','B) 2003, İngiltere','C) 2006, Çin','D) İnsan klonlama henüz gerçekleşmedi'],'Dogru Cevap':'d'},

]







def random_quest():
    return random.randint(0,11)



def random_questing(ask):
    print(all_quest[ask]['Soru'])
    print(all_quest[ask]['secenekler'])
    
def answer_input():
    print('\n','``'*50,'\n')
    return input('\nCevabi Giriniz\n').lower() 

def quest_controll(answer):
     total_quest = 0
     total_true = 0
     if answer == all_quest[ask]['Dogru Cevap']:
         total_true += 1
         total_quest += 1
         print('\n','``'*50,'\n')
         print('\nDogru Cevap Verdiniz\n')
         print('\n','``'*50,'\n')
     else:
         total_quest += 1
         print('\n','``'*50,'\n')
         print('\nYanlis Cevap Verdiniz\n')
         print('\n','``'*50,'\n')
         print(all_quest[ask]['Dogru Cevap'])
         print('\n','``'*50,'\n')
     return total_true/total_quest

def continue_input():
    print('\n','``'*50,'\n')
    return input('Devam Etmek Icin <c> Etmemek Icin <nc>').lower()
     

def continue_controll(continue_):
    if continue_ == 'c':
        print('\n','``'*50,'\n')
    elif continue_ == 'nc':
        print('\n','``'*50,'\n')
        print('Cikiliyo...')
        return False


        


while True:
    ask = random_quest()

    random_questing(ask)

    answer = answer_input()

    quest_controll(answer)

    continue_ = continue_input()

    continue_controll(continue_)
  


    
    