import random

options = ['Tas','Kagit','Makas'] 

choose = input('Tas = 1\nKagit = 2\nMaks = 3\n')

point = 0

enemy_point = 0

while True:
      choose_enemy = random.choice(options)
      # Kazanama
      if choose =='1' and choose_enemy =='Makas' and point != 3 and enemy_point != 3 :
        print('Bu el Kazandin\n')
        point += 1
        print('\n','Tas , Puanin : ',point,'\n')
        print('\n',choose_enemy,'Dusman Puan : ',enemy_point,'\n')
        
  
      elif choose =='2' and choose_enemy =='Tas' and point != 3 and enemy_point != 3 :
        print('Bu el Kazandin\n')
        point += 1
        print('\n','Kagit , Puanin : ',point,'\n')
        print('\n',choose_enemy,'Dusman Puan : ',enemy_point,'\n')
        

      elif choose =='3' and choose_enemy =='Kagit' and point != 3 and enemy_point != 3 :
        print('Bu el Kazandin\n')
        point += 1
        print('\n','Makas , Puanin : ',point,'\n')
        print('\n',choose_enemy,'Dusman Puan : ',enemy_point,'\n')
        
        

#KAYBETME

      elif choose =='1' and  choose_enemy == 'Kagit'and point != 3 and enemy_point != 3 :
        print('Bu el kaybetin\n')
        enemy_point += 1
        print('\n','Tas , Puanin : ',point,'\n')
        print('\n',choose_enemy,'Dusman Puan : ',enemy_point,'\n')
        


      elif choose =='2' and  choose_enemy == 'Makas'and point != 3 and enemy_point != 3 :
        print('Bu el kaybetin\n')
        enemy_point += 1
        print('\n','Kagit , Puanin : ',point,'\n')
        print('\n',choose_enemy,'Dusman Puan : ',enemy_point,'\n')
        


      elif choose =='3' and choose_enemy == 'Tas'and point != 3 and enemy_point != 3 :
        print('Bu el kaybetin\n')
        enemy_point += 1
        print('\n','Makas , Puanin : ',point,'\n')
        print('\n',choose_enemy,'Dusman Puan : ',enemy_point,'\n')

      
#BERARBERE

      elif choose =='1' and  choose_enemy == 'Tas'and point != 3 and enemy_point != 3 :
        print('Berabere\n')
        print('\n','Tas , Puanin : ',point,'\n')
        print('\n',choose_enemy,'Dusman Puan : ',enemy_point,'\n')
        


      elif choose =='2' and  choose_enemy == 'Kagit'and point != 3 and enemy_point != 3 :
        print('Berabere\n')
        print('\n','Kagit , Puanin : ',point,'\n')
        print('\n',choose_enemy,'Dusman Puan : ',enemy_point,'\n')
        


      elif choose =='3' and choose_enemy == 'Makas'and point != 3 and enemy_point != 3 :
        print('Berabere\n')
        print('\n','Makas , Puanin : ',point,'\n')
        print('\n',choose_enemy,'Dusman Puan : ',enemy_point,'\n')


     

      






      else :
         print('Oyle bir islem yok\n')

           




      if point == 3 :
        print('Kazandin')
        vote = input('\nTekrar aoynamak icini <E> oynaamamk icini <H>\n')
        if vote == 'E':
            print('\nTekrar Basliyo\n')
            point = 0
            enemy_point = 0
        elif vote == 'H':
           print('\nCikiliyo...\n')
           break
        else:
           print('\nYanlsi islem\n')
           vote = input('\nTekrar aoynamak icini <E> oynaamamk icini <H>\n')
           

      elif enemy_point == 3:
         print('Kaybettin')
         vote = input('\nTekrar aoynamak icini <E> oynaamamk icini <H>\n')
         if vote == 'E':
            print('\nTekrar Basliyo\n')
            point = 0
            enemy_point = 0
         elif vote == 'H':
           print('\nCikiliyo\n')
           break
         else:
           print('\nYanlsi islem\n')
           vote = input('\nTekrar aoynamak icini <E> oynaamamk icini <H>\n')
      
      
         
      
      if point != 3 or enemy_point != 3:
         choose = input('Tas = 1\nKagit = 2\nMaks = 3\n')