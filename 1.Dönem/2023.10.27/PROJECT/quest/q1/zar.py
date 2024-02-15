import random


quest = int(input('Kac defa zar atmak istiyon\n'))

for zar in range(1,quest):
    zar = random.randint(1,6)
    print(zar)