from tkinter import *

class juros:

    def __init__(self):
        
        #chamar janela principal
        self.windowCalcJuros()
        """a = self.calcMelhorValor(800, 2)
        print(a)"""

    def windowCalcJuros(self):

        fontStyle = 'Arial 12'

        self.window = Tk()
        self.window.geometry('700x500')
        self.window.title('CALCULADORA DE JUROS - MERCADO PAGO')


        #Informar o valor da Compra
        lbl = Label(text='Informe o Valor que Deseja Receber: ', font=fontStyle)
        lbl.pack()

        self.etValor = Entry(font=fontStyle)
        self.etValor.pack()

        #Botao para gerar simulação
        btSimulation = Button(text='Gerar Simulação', fg='red', font='Arial 12 bold', command=lambda: exibirDados())
        btSimulation.pack(pady=5)
        
        #exibidor de dados
        ltDados = Listbox(width=80, height=30, font='Courier 10', bg='black', fg='white')
        ltDados.pack(pady=5)

        def exibirDados():
            
            #limpar listbox
            ltDados.delete(0, 'end')

            info = self.funcaoCalc(float(self.etValor.get()))

            #adcionar lnihas no listbox
            for pos, i in enumerate(info):
                ltDados.insert(pos, i)

            self.etValor.delete(0, END)


        self.window.mainloop()

    def funcaoCalc(self, valorCompra):
        
        listaValores = []

        self.tablaJuros = { 2:4.09, 
                            3:5.41, 
                            4:6.70, 
                            5:7.96, 
                            6:9.20, 
                            7:10.41, 
                            8:11.61, 
                            9:12.78, 
                            10:13.92, 
                            11:15.05, 
                            12:16.15}

        self.valorDias = {1:4.74, 15:3.79, 30:3.60}

        for valor in [1, 15, 30]:
            
            v = '                       RECEBER COM {} DIAS'.format(valor)
            listaValores.append(v)

            for i in range(2, 13):
                
                #calcular juros, Valor real e valor de Cada parcela
                vJuros = ((self.valorDias[valor] + self.tablaJuros[i]) / 100) * valorCompra
                vReceber = valorCompra - vJuros
                vParcela = valorCompra / i
               
                #Adicionar valor a lista de exibição
                v = '       {} x {:.2f} = {:.2f} -- Juros = {:.2f} -- Cobrar = {:.2f}'.format(i, vParcela, vReceber, vJuros, self.calcMelhorValor(valor, valorCompra, i))
                                    
                #incluir na lista
                listaValores.append(v)

            #espaçar os conjunto de dados
            listaValores.append('')

        #retorna uma lista de valores
        return listaValores

    def calcMelhorValor(self, diaReceber, valor, i):
        
        v = 0
        vInicial = valor

        while True:
            vJuros = ((self.valorDias[diaReceber] + self.tablaJuros[i]) / 100) * valor
            vReceber = valor - vJuros

            if vReceber >= vInicial:
                v = valor
                break

            else:
                #print(valor)
                valor += 1

        #retorna o valor que deve-se ser cobrado
        return v

#chama a classe principal
juros()

