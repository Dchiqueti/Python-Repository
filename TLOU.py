# This is practice code inspired in The Last Of Us
# I did it to practice the While Loop, also used some libraries like random and time
# Watch this running on CMD https://www.youtube.com/watch?v=BeDiHUhYXHs

import random
import time
from os import system

system('cls')
infected = int(input('Digite a quantidade de infectados que Joel e Ellie irão enfrentar: '))
if infected >= 10:
    
    print('\nNossa!', infected, 'infectados, vai ser complicado')

elif infected < 3:
    
    print('Só isso?', infected, 'é moleza')

else: 
    
    print('\n', infected, 'infectados, é uma briga justa')

time.sleep(2)
while infected != 0:
    
    custom = random.randint(1,5)
    if custom == 1 and infected >= 2:
        
        print('\n Joel dispersa um tiro de doze que mata dois infectados de uma vez!')
        infected -= 2
        
    elif custom == 2:
        
        print('\n Joel está em apuros, um infectado está em cima dele!')
        time.sleep(2)
        print(' Ellie esfaqueia o infectado e ajuda Joel')
        infected -= 1
    
    elif custom == 3 and infected <= 4:

        print('\n Droga, chegou mais um!')
        infected += 1

    ## Definir 2 entre as 5 possibilidades para ser o evento com maior probabilidade
    elif custom == 4 or custom == 5:
        
        print('\n Joel atira com a pistola em um infectado')
        infected -=1
    
    else:
        continue
    print(' infectados restantes:', infected)
    time.sleep(2)

print('\n Finalmente acabou!')
