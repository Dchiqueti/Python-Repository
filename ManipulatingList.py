# Manipulating a List
# In this code i focus in creating a empty list and manipulate it
# Watch the demonstration video: https://www.youtube.com/watch?v=nEkkPd75voI


from os import system
import time

def getNames():
    
    global namesList
    namesList = []
    listSize = len(namesList)
    namesReady = False
    while not namesReady:
    
        name = (input('\n Digite o nome a ser adicionado na lista: '))
        namesList.append(name.capitalize())
        replied = False
        while not replied:
            
            ready = input('\n A lista está com %r elementos, adicionar mais nomes a lista? (S ou N) ' %(len(namesList)))
            if ready == 'N' or ready == 'n':

                replied = True
                namesReady = True
                
            elif ready == 'S' or ready == 's':
                
                replied = True

            else:

                print('Não compreendi, tentaremos novamente')
    
    return print('\n Essa é sua lista', namesList)

def nameAlfaSort(array):
    
    size = len(array)
    for i in range(size):
        
        for j in range(0, size-1-i):
            
            if array[j] > array[j+1]:
                
                array[j], array[j+1] = array[j+1], array[j]

    return print('\n Essa é a lista organizada em ordem alfabética', array)

def searchLetter():
    
    letter = input('\n Digite a letra a ser pesquisada: ')
    for x in namesList:

        if letter.lower() in x.lower():
            print('\n Foi encontrado %r indice %s da lista' %(x, namesList.index(x)))

def searchIndex(): 
    
    a = len(namesList) - 1
    indexNum = int(input('\n Digite o indice a ser pesquisado entre 0 e %s: ' %(a)))
    if indexNum <= a: print('\n Aqui está o nome presente no indice: ', namesList[indexNum])
    
print('Iremos gerar uma lista de nomes')
getNames()
jobDone = False
while not jobDone:
    
    time.sleep(3)
    system('cls')
    print('\n Lista:', namesList)
    print('\n Ações disponíveis para a lista:')
    print('\nOrganizar em ordem alfabética(1) \nConsulta por letra ou nome(2) \nConsulta por indice(3) \nRealizar todos(4) \nSair(5)')
    action = int(input('Digite a ação desejada: '))
    if action == 1: nameAlfaSort(namesList)
    elif action == 2: searchLetter()
    elif action == 3: searchIndex()
    elif action == 4: nameAlfaSort(namesList), searchLetter(), searchIndex()
    elif action == 5: jobDone = True
    else: print('Não compreendi, tentaremos novamente')
