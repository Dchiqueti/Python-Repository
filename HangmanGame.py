# Hangman Game (Jogo da Forca) 

from ntpath import join
from os import system,name
import random
import time

board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |      ''Ah não...''
/|\  |
/ \  |
     |
=========''', '''

 +---+
 |   |
     |  ''Uhull''
\O/  |
 |   |
/ \  |
=========''']

wordsList = ['abacate', 'baixo', 'caminho', 'doceria', 'escola','fazenda','gente','humano','igualdade','juventude','liberdade','mulher',
               'natureza','obrigado','protegido','queijo','riacho','saudade','terra','universo','vontade','xadrez','yoga','zangado']

def clearOutput():

    if name == 'nt': _ = system('cls')
    else: _ = system('clear')

class Hangman():

	# Método Construtor
    def __init__(self):
          
          
          self.word = random.choice(wordsList)
          self.word.split()
          self.rightLetters = []
          for x in self.word: self.rightLetters.append('_')
          self.wrongLetters = []
          self.failed = 0
            	
    def guessLetter(self):

        letter = input(' Digite a letra que você deseja tentar:' )
        letter = letter.lower()
        if letter in self.wrongLetters or letter in self.rightLetters: print(' Você já tentou essa letra')
        elif letter in self.word:
            
            print('\n Boa tentativa, você adivinhou a letra', letter)
            index = 0
            for x in self.word:
               
                if x == letter: self.rightLetters[index] = letter
                index += 1

        elif len(letter) > 1: print('\n Por favor, digite apenas uma letra')
        else:
            
            self.wrongLetters.append(letter)
            self.failed += 1
            chances = 6 - self.failed
            print('\n OpS... %s não está na palavra \n Tentativas restantes: %d' %(letter, chances))

        time.sleep(2)
        clearOutput()

    def gameOver(self):
        
        if self.failed == 6 or '_' not in self.rightLetters: return True
        else: return False

    def gameEnding(self):
        
        if '_' not in self.rightLetters:
            print(board[7])
            print(' \n\n Você acertou a palavra %s!' %(self.word))
            print(' Parabéns! Você ganhou da forca!')

        else: print('%s \n \n A palavra era %s \n Você foi enforcado, tente novamente' %(board[6],self.word))

    def gameStatus(self):
     
        print(board[self.failed])
        if self.failed != 0: print('\n Tentativas:', self.wrongLetters)
        print('\n Palavra:', self.rightLetters)
  
def main():
    
    clearOutput()
    jogo1 = Hangman()

    while not jogo1.gameOver():

        jogo1.gameStatus()
        jogo1.guessLetter()
        

    jogo1.gameEnding()

if __name__ == '__main__': main()