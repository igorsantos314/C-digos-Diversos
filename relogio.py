from datetime import datetime
import _thread
from time import sleep
import os
now = datetime.now()

matriz = []

def zero():
    mZero = []

    mZero.append(['*' for i in range(7)])
    mZero.append(['*','*',' ',' ',' ','*','*'])
    mZero.append(['*','*',' ',' ',' ','*','*'])
    mZero.append(['*','*',' ',' ',' ','*','*'])
    mZero.append(['*','*',' ',' ',' ','*','*'])
    mZero.append(['*','*',' ',' ',' ','*','*'])
    mZero.append(['*','*',' ',' ',' ','*','*'])
    mZero.append(['*' for i in range(7)])

    matriz.append(mZero)

def um():
    mZero = []

    mZero.append(['*' for i in range(2)])
    mZero.append(['*','*'])
    mZero.append(['*','*'])
    mZero.append(['*','*'])
    mZero.append(['*','*'])
    mZero.append(['*','*'])
    mZero.append(['*','*'])
    mZero.append(['*' for i in range(2)])

    #for i in mZero:
    #    print(*i)
    matriz.append(mZero)

def dois():
    mZero = []

    mZero.append(['*' for i in range(7)])
    mZero.append([' ',' ',' ',' ',' ','*','*'])
    mZero.append([' ',' ',' ',' ',' ','*','*'])
    mZero.append(['*','*','*','*','*','*','*'])
    mZero.append(['*','*','*','*','*','*','*'])
    mZero.append(['*','*',' ',' ',' ',' ',' '])
    mZero.append(['*','*',' ',' ',' ',' ',' '])
    mZero.append(['*' for i in range(7)])

    matriz.append(mZero)

def tres():
    mZero = []

    mZero.append(['*' for i in range(7)])
    mZero.append([' ',' ',' ',' ',' ','*','*'])
    mZero.append([' ',' ',' ',' ',' ','*','*'])
    mZero.append([' ',' ',' ','*','*','*','*'])
    mZero.append([' ',' ',' ','*','*','*','*'])
    mZero.append([' ',' ',' ',' ',' ','*','*'])
    mZero.append([' ',' ',' ',' ',' ','*','*'])
    mZero.append(['*' for i in range(7)])

    matriz.append(mZero)

def quatro():
    mZero = []

    mZero.append(['*',' ',' ',' ',' ','*','*'])
    mZero.append(['*',' ',' ',' ',' ','*','*'])
    mZero.append(['*',' ',' ',' ',' ','*','*'])
    mZero.append(['*','*','*','*','*','*','*'])
    mZero.append(['*','*','*','*','*','*','*'])
    mZero.append([' ',' ',' ',' ',' ','*','*'])
    mZero.append([' ',' ',' ',' ',' ','*','*'])
    mZero.append([' ',' ',' ',' ',' ','*','*'])

    matriz.append(mZero)

def cinco():
    mZero = []

    mZero.append(['*' for i in range(7)])
    mZero.append(['*','*',' ',' ',' ',' ',' '])
    mZero.append(['*','*',' ',' ',' ',' ',' '])
    mZero.append(['*','*','*','*','*','*','*'])
    mZero.append(['*','*','*','*','*','*','*'])
    mZero.append([' ',' ',' ',' ',' ','*','*'])
    mZero.append([' ',' ',' ',' ',' ','*','*'])
    mZero.append(['*' for i in range(7)])

    matriz.append(mZero)

def seis():
    mZero = []

    mZero.append(['*' for i in range(7)])
    mZero.append(['*','*',' ',' ',' ',' ',' '])
    mZero.append(['*','*',' ',' ',' ',' ',' '])
    mZero.append(['*','*','*','*','*','*','*'])
    mZero.append(['*','*','*','*','*','*','*'])
    mZero.append(['*','*',' ',' ',' ','*','*'])
    mZero.append(['*','*',' ',' ',' ','*','*'])
    mZero.append(['*' for i in range(7)])

    matriz.append(mZero)

def sete():
    mZero = []

    mZero.append(['*' for i in range(7)])
    mZero.append([' ',' ',' ',' ',' ','*','*'])
    mZero.append([' ',' ',' ',' ',' ','*','*'])
    mZero.append([' ',' ',' ',' ',' ','*','*'])
    mZero.append([' ',' ',' ',' ',' ','*','*'])
    mZero.append([' ',' ',' ',' ',' ','*','*'])
    mZero.append([' ',' ',' ',' ',' ','*','*'])
    mZero.append([' ',' ',' ',' ',' ','*','*'])

    matriz.append(mZero)

def oito():
    mZero = []

    mZero.append(['*' for i in range(7)])
    mZero.append(['*','*',' ',' ',' ','*','*'])
    mZero.append(['*','*',' ',' ',' ','*','*'])
    mZero.append(['*','*','*','*','*','*','*'])
    mZero.append(['*','*','*','*','*','*','*'])
    mZero.append(['*','*',' ',' ',' ','*','*'])
    mZero.append(['*','*',' ',' ',' ','*','*'])
    mZero.append(['*' for i in range(7)])

    matriz.append(mZero)

def nove():
    mZero = []

    mZero.append(['*' for i in range(7)])
    mZero.append(['*',' ',' ',' ',' ','*','*'])
    mZero.append(['*',' ',' ',' ',' ','*','*'])
    mZero.append(['*','*','*','*','*','*','*'])
    mZero.append(['*','*','*','*','*','*','*'])
    mZero.append([' ',' ',' ',' ',' ','*','*'])
    mZero.append([' ',' ',' ',' ',' ','*','*'])
    mZero.append(['*' for i in range(7)])

    matriz.append(mZero)

def pontos():
    mZero = []

    mZero.append([' ' for i in range(2)])
    mZero.append(['*','*'])
    mZero.append(['*','*'])
    mZero.append([' ',' '])
    mZero.append([' ',' '])
    mZero.append(['*','*'])
    mZero.append(['*','*'])
    mZero.append([' ' for i in range(2)])

    #for i in mZero:
    #    print(*i)
    matriz.append(mZero)


def createMatriz(tempo):
    global matriz

    matriz = []

    """for i in range(30):
        matrizSecundaria = [' ' if j == 3 and len(matriz) else '*' for j in range(70) ]

        matriz.append(matrizSecundaria)

    for i in matriz:
        print(*i)"""

    for i in tempo:
        if i == '0':
            zero()

        elif i == '1':
            um()

        elif i == '2':
            dois()
            
        elif i == '3':
            tres()

        elif i == '4':
            quatro()

        elif i == '5':
            cinco()

        elif i == '6':
            seis()

        elif i == '7':
            sete()

        elif i == '8':
            oito()

        elif i == '9':
            nove()

        elif i == ':':
            pontos()
    
    criarRelogio()

def criarRelogio():
    linha = ''
    #print(matriz[0][0])
    for l in range(8):
        for i in range(len(matriz)) :
            for i in matriz[i][l]:
                linha += i

            linha += '   '
        
        linha += '\n'

    print(linha)

def exibir():
    createMatriz('{}:{}:{}'.format(now.hour,now.minute,now.second))
   
exibir()
sleep(3)
exibir()