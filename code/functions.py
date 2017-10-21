#IMPORTAÇÕES:
#PDF MINER
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
#OUTROS
import re
from fuzzywuzzy import fuzz
import pickle

#FUNÇÕES:
def getText(pdfname, filename): #Função que extrai o texto do pdf, usando os parâmetros padrão da biblioteca pdfminer
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'latin1'
    laparams = LAParams()
    path = "C:/Users/Luke/Documents/Prog/Python/Sis500/pdf/"+pdfname+".pdf"
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb') #Pega o arquivo do pdf no caminho especificado
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    #Roda um loop, usando todos os atributos anteriores, interpretando o pdf por página e realizando a conversão
    for pagenumber, page in enumerate(PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True)):
        if pagenumber < 16: #Pula as primeiras 16 páginas, que não possuem nenhuma pergunta/resposta
            pass
        else:
            if pagenumber >= 100:
                retstr.write("\n 500pr_pgnumber" + str(pagenumber) +"  ")
            else:
                retstr.write("\n 500pr_pgnumber0" + str(pagenumber) +"  ")
            interpreter.process_page(page)


    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()

    with open("C:/Users/Luke/Documents/Prog/Python/Sis500/txt/"+filename+".txt", "w") as textFile:
        textFile.write(text)


def getAnswers(filename): #Função que separa as perguntas e respostas do texto minerado do pdf
    filename = filename
    filepath = "C:/Users/Luke/Documents/Prog/Python/Sis500/txt/" + filename+ ".txt"

    respostas = []
    perguntas = []
    paginas = []

    file = open(filepath,"r")#Abre o arquivo de texto
    file = file.read()
    rgx = re.compile('(?<=\.)[^.]*$') #Compilação do regex a ser utilizado no loop

    for i in range(0,507):#até 507; Total de iterações necessárias para pegar todas as perguntas e respostas
        splitString = file.split("?")[i]
        respostas.append(splitString) #As duas listas recebem a mesma string separadas no "?"
        perguntas.append(splitString)

        respostas[i] = re.sub(rgx,'', respostas[i]) #Porém uma pega o regex sem a pergunta(a resposta)
        perguntas[i] = rgx.findall(perguntas[i]) #e a outra pega o regex que só dá match na pergunta(a pergunta)

    perguntas[0] = "Qual a origem mais provável do algodoeiro" #Por motivos específicos, o código não consegue pegar a primeira pergunta, então temos que colocá-la manualmente
    respostas.pop(0) #Pelo mesmo motivo, a primeira resposta é nula, então apagamos ela manualmente


    conjunto = [perguntas,respostas]
    filename = filename.replace("txt","procTxt")
    filepath = "C:/Users/Luke/Documents/Prog/Python/Sis500/txt/" + filename + ".txt"
    with open(filepath, 'wb') as fp:
       pickle.dump(conjunto, fp)

def run(filename):
    filepath = "C:/Users/Luke/Documents/Prog/Python/Sis500/txt/" + filename + ".txt"
    with open(filepath, 'rb') as file:
        lista = pickle.load(file)

    perguntas = lista[0]
    respostas = lista[1]
    bestMatchIndex = 0
    bestRatio = 0

    while True:
        perguntaUser = input("Digite a sua pergunta: ")
        for index, pergunta in enumerate(perguntas):
            ratio = fuzz.ratio(perguntaUser, pergunta)
            if ratio > bestRatio:
                bestMatchIndex = index
                bestRatio = ratio

        print("\nPergunta relacionada: "+ str(perguntas[bestMatchIndex]) +
          "\nResposta relacionada: " + respostas[bestMatchIndex])
        print("\nProximidade da pergunta: " + str(bestRatio))


def checkRatio(perguntaUser):
    pass

