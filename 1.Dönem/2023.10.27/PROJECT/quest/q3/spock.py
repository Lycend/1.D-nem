import random

ai_quest = ['tas','kagit','makas','spock','kertenkele']


print(ai_quest)



player_answer = input('\nSecim Yapiniz\n').lower()
while True:
    ai_answer = random.choice(ai_quest)
    #Tas
    if player_answer == 'tas':
     
      if player_answer == ai_answer     :
          print('\nBu eli Berabere\n')
      elif player_answer == 'tas' and ai_answer == 'makas' or player_answer == 'tas' and ai_answer == 'makas' :
         print('\nBu eli Kazandin\n')
      elif player_answer == 'tas' and ai_answer == 'kagit' or player_answer == 'tas' and ai_answer == 'spock':
         print('\nBu Eli Kaybettin\n')
     

    #Kagit
    elif player_answer == 'kagit':
      
      if player_answer == ai_answer     :
          print('\nBu eli Berabere\n')
      elif player_answer == 'kagit' and ai_answer == 'tas' or player_answer == 'kagit' and ai_answer == 'spock' :
         print('\nBu eli Kazandin\n')
      elif player_answer == 'kagit' and ai_answer == 'makas' or player_answer == 'kagit' and ai_answer == 'kertenkele':
         print('\nBu Eli Kaybettin\n')
     

     #Makas
    elif player_answer == 'makas':
     
      if player_answer == ai_answer     :
          print('\nBu eli Berabere\n')
      elif player_answer == 'makas' and ai_answer == 'kagıt' or player_answer == 'makas' and ai_answer == 'kertenkele' :
         print('\nBu eli Kazandin\n')
      elif player_answer == 'makas' and ai_answer == 'tas' or player_answer == 'makas' and ai_answer == 'spock':
         print('\nBu Eli Kaybettin\n')
      
    
    #Kertenkele
    elif player_answer == 'kertenkele':
     
      if player_answer == ai_answer     :
          print('\nBu eli Berabere\n')
      elif player_answer == 'kertenkele' and ai_answer == 'spock' or player_answer == 'kertenkele' and ai_answer == 'kagid' :
         print('\nBu eli Kazandin\n')
      elif player_answer == 'kertenkele' and ai_answer == 'tas' or player_answer == 'kertenkele' and ai_answer == 'makas':
         print('\nBu Eli Kaybettin\n')
     


    #Spock
    elif player_answer == 'spock':
     
      if player_answer == ai_answer     :
          print('\nBu eli Berabere\n')
      elif player_answer == 'spock' and ai_answer == 'makas' or player_answer == 'spock' and ai_answer == 'tas' :
         print('\nBu eli Kazandin\n')
      elif player_answer == 'spock' and ai_answer == 'kertenkele' or player_answer == 'spock' and ai_answer == 'kagit':
         print('\nBu Eli Kaybettin\n')
      

    

    else:
       print('Yanlis tuslama yapmis olabilirsiniz\n')


    vote = input('Tekrar Oynamak icin <E> oynamamak icin <H>\n')

    if vote == 'E':
       print('Tekrar Oynaniyo\n')
       player_answer = input('\nSecim Yapiniz\n').lower()
    elif vote == 'H':
       print('Cikiliyo...')
       break
    else:
       print('Yanlis Tuslama Ypmis Olabilirsiniz')
       vote = input('Tekrar Oynamak icin <E> oynamamak icin <H>\n')
       
    



