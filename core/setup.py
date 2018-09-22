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
    for i in range(0,len(lista)-1):
        getAnswers(lista[i][0], lista[i][3])

#PEGA TODOS OS TXTS E PROCESSA AS PERGUNTAS E RESPOSTAS E JOGA EM UMA LISTA ÚNICA DE TODAS AS PERGUNTAS
def mergeAllText():
    listaCompleta = []
    listaLivros = importaLista()
    for i in range(0,len(listaLivros)-1):
        filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "txt", "500pr_procTxt_" + listaLivros[i][0] + ".txt"))
        with open(filepath, 'rb') as file:
            listaCompleta.extend(pickle.load(file))
    filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "txt", "500pr_procTxt_" + "todos" + ".txt"))
    with open(filepath, 'wb') as fp:
       pickle.dump(listaCompleta, fp)


#pdf2text()
#text2answers()
#mergeAllText()

#getAnswers(importaLista()[0][0], importaLista()[0][3])

#RICINO
#getText("ricino",0) #EM ESPANHOL
#getAnswers("ricino", "XXXXXXXXXXXXXXXXXXXXXXX") #EM ESPANHOL
#print(run("como funciona o plantio","aaaaasuperlivro"))