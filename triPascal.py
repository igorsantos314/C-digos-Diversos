def calcular(nLinhas):
    lista = [[1], [1,1]]

    for i in range(nLinhas):
        ultimaLista = [1]

        for i in range(len(lista[-1])):
            if i < (len(lista[-1]) - 1):
                res = lista[-1][i] + lista[-1][i+1]
                ultimaLista.append(res)

        ultimaLista.append(1)
        lista.append(ultimaLista)

    for pos,i in enumerate(lista):
        print('Linha {} - '.format(pos+1), *i)

def menu():
    nLinhas = int(input("           --> Digite a Quantidade de Linhas: "))
    calcular(nLinhas)

menu()