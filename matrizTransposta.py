mTeste = [  [2,4,1],
            [6,8,3],
            [10,12,4],
            [11,8,5]]

def transpor():

    mResultante = [[] for l in range(len(mTeste[0])) ]
    print(mResultante)

    for j in range(len(mTeste)):
        for i in range(len(mTeste[0])):
            mResultante[i].append(mTeste[j][i])

    for l in mResultante:
        print(l)

transpor()