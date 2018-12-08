from core.functions import *
from core.data import *

#Importa a lista de livros que está no arquivo "data"
def importaLista():
    return getListaLivros()

#Itera por todos os pdfs na lista e transforma em texto
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
#text2answers()