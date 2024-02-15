def numbers_prime(numbers):
    for i in range(2,numbers):
            if numbers % i == 0:
                  return False
            return True

for i in range(100):
        if  numbers_prime(i):
               print(i)
