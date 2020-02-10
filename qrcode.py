import pyqrcode
from tkinter import *

def gerar():
    link = pyqrcode.create("nomeLink")
    link.svg('uca-url.svg', scale=8)

    codigo = link.png(quiet_zone=1)
    
    lblCodigo['text'] = codigo

def setJanela():
    global lblCodigo 

    janela = Tk()
    janela.geometry("500x500")

    lblCodigo = Label(text='')
    lblCodigo.pack()

    btCodigo = Button(text="Ver Código", command = gerar)
    btCodigo.pack()

    janela.mainloop()

setJanela()