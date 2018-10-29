from core.functions import *
from core.data import *
import os, pickle
#IMPORTA A LISTA DE LIVROS
def importaLista():
    return getListaLivros()

#PEGA TODOS OS PDFS E CONVERTE EM TXT
def pdf2text():
    lista = importaLista()
    for i in range(0,len(lista)-1):
        getText(lista[i][0], lista[i][1], lista[i][2])


#PEGA TODOS OS TXTS E PROCESSA AS PERGUNTAS E RESPOSTAS, E GERA O PROCTXT SINGULAR POR LIVRO
def text2answers():
    lista = importaLista()
    for i in range(0,len(lista)):
        getAnswers(lista[i][0], lista[i][3])
        print(lista[i][0])


#pdf2text()
text2answers()

#getAnswers(importaLista()[0][0], importaLista()[0][3])

#RICINO
#getText("ricino",0) #EM ESPANHOL
#getAnswers("ricino", "XXXXXXXXXXXXXXXXXXXXXXX") #EM ESPANHOL
