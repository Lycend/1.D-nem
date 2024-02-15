import math

calculator = input('+ = toplama\n- = çıkarma\n* = çarpma\n/ = bölme\n** = üs alma\nK = karkök\nq = çıkış\n\n')


add = ('+')

minus = ('-')

mult = ('*')

divide = ('/')

square_root = ('K')

us_alma = ('**')

exite = ('q')

exite2=("Q")


while calculator != exite :

      if calculator == add:
        
        number_1 = int(input('1. sayıyı giriniz.\n\n'))

        number_2 = int(input('2. sayıyı giriniz.\n\n'))
        operation_add = number_1 + number_2
        print('\n\n',operation_add,'\n\n')


      elif calculator == minus:
          
          number_1 = int(input('1. sayıyı giriniz.\n\n'))

          number_2 = int(input('2. sayıyı giriniz.\n\n'))
          operation_minus = number_1 - number_2
          print('\n\n',operation_minus,'\n\n')


      elif calculator == mult :
          
           number_1 = int(input('1. sayıyı giriniz.\n\n'))
 
           number_2 = int(input('2. sayıyı giriniz.\n\n'))
           operation_mult = number_1 * number_2
           print('\n\n',operation_mult,'\n\n')



   

      elif calculator == divide:
          
          
           number_1 = int(input('1. sayıyı giriniz.\n\n'))

           number_2 = int(input('2. sayıyı giriniz.\n\n'))
           operation_divide = number_1 / number_2
           print('\n\n',operation_divide,'\n\n'),
      
      
      elif calculator == divide and number_2 == 0:
             
              number_1 = int(input('1. sayıyı giriniz.\n\n'))

              number_2 = int(input('2. sayıyı giriniz.\n\n'))
              
              print('\n\n',number_1,'0"a bölemezsin ','\n\n')   

      elif calculator == us_alma:

      
         number_1 = int(input('1. sayıyı giriniz.\n\n'))
 
         number_2 = int(input('2. sayıyı giriniz.\n\n'))
         operation_us_alma = number_1 ** number_2
         print('\n\n',operation_us_alma,'\n\n')


      elif calculator == square_root:
         
           number_1 = int(input('1. sayıyı giriniz.\n\n'))
           operation_square_root = math.sqrt(number_1)
      

           print('\n\n',operation_square_root,'\n\n')

      elif calculator == exite :
          print('\n\nUygulamadan Çıkılmıştır :) \nLütfen tekrar geliniz\n\n')    

          

      else:
          print('\n\nBöyle bir işlem yok başka bir işlem deneyiniz','\n\n')    
     
      calculator = input('+ = toplama\n- = çıkarma\n* = çarpma\n/ = bölme\n** = üs alma\nK = karkök\nq = çıkış\n\n')
