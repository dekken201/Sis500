#IMPORTAÇÕES:
#PDF MINER - pacotes necessários para realizar extração do texto dos PDFs
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
#OUTRAS IMPORTAÇÕES
import re  #Importa o módulo interno para uso de expressões regulares
from fuzzywuzzy import fuzz  #Importa a biblioteca "fuzzyWuzzy"(distãncia de levenshtein)
import pickle  #importa pickle(serialização e deserialização de arquivos)
import os  #biblioteca para comunicação com o sistema(salvamento e abertura de arquivos)
from core.data import *  #importa as funções e dados contidos neste projeto

basepath = os.path.dirname(__file__)  #Cria o diretório base com relação ao diretório atual deste arquivo


#FUNÇÕES:
def getText(pdfname,pageZero,pageEnd): #Função que extrai o texto do pdf, usando os parâmetros padrão da biblioteca pdfminer
    global basepath
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    filepath = os.path.abspath(os.path.join(basepath, "..", "pdf", "500pr","500pr_"+pdfname+".pdf"))
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(filepath, 'rb') #Pega o arquivo do pdf no caminho especificado
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    #Roda um loop, usando todos os atributos anteriores, interpretando o pdf por página e realizando a conversão
    for pagenumber, page in enumerate(PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True)):
        if (pagenumber < pageZero -1) or (pagenumber >= pageEnd): #Pula as primeiras páginas, que não possuem nenhuma pergunta/resposta
            pass
        else:
            #Enquanto itera pelas páginas, adiciona ao topo de capa uma uma string reconhecível para salvarmos o número da página
            if pagenumber >= 100:
                retstr.write("\n 500pr_pgnumber" + str(pagenumber + 1) +"\n")
            else:
                retstr.write("\n 500pr_pgnumber0" + str(pagenumber + 1) +"\n")
            interpreter.process_page(page)

    text = retstr.getvalue()  #salva o texto gerado pela iteração anterior na variável text

    fp.close()
    device.close()
    retstr.close()
    filepath = os.path.abspath(os.path.join(basepath, "..", "txt" , "500pr_txt_" + pdfname + ".txt"))
    try:
        with open(filepath, "w") as textFile:
            textFile.write(text)
    except UnicodeEncodeError:
        with open(filepath, "w",encoding='utf-8') as textFile:
            textFile.write(text)
    print(pdfname+ " - ok")


def getAnswers(filename,perguntaZero): #Função que separa as perguntas e respostas do texto minerado do pdf
    global basepath
    filepath = os.path.abspath(os.path.join(basepath, "..", "txt", "500pr_txt_" + filename + ".txt"))

    respostas = []
    perguntas = []
    paginas = []
    nomeLivro = []
    nomeLivroTratado = ""
    try:
        file = open(filepath,"r")#Abre o arquivo de texto
        file = file.read()
    except UnicodeDecodeError:
        file = open(filepath, "r",encoding='utf-8')
        file = file.read()

    rgx = re.compile('(?<=\.)[^.]*$')  # Compilação do regex a ser utilizado no loop
    rgxPage = re.compile('(?<=500pr_pgnumber)\w{3}')
    rgxSplit = '(?=\?\n)'

    i = 0
    while True:
        try:
            #splitString = file.split("?")[i]
            splitString = re.split(rgxSplit, file)[i]
        except IndexError:
            break

        respostas.append(splitString) #As duas listas recebem a mesma string separadas no "?"
        perguntas.append(" ".join(splitString.split())) #Retira grande parte do espaço em branco e desnecessário da string perguntas
        paginas.append(splitString)

        respostas[i] = re.sub(rgx,'', respostas[i]) #Porém uma pega o regex sem a pergunta(a resposta)
        perguntas[i] = rgx.findall(perguntas[i]) #e a outra pega o regex que só dá match na pergunta(a pergunta)
        paginas[i] = rgxPage.findall(splitString)

        respostas[i].replace('\\n', '\n')
        i += 1


    perguntas[0] = perguntaZero #Por motivos específicos, o código não consegue pegar a primeira pergunta, então temos que colocá-la manualmente
    respostas.pop(0) #Pelo mesmo motivo, a primeira resposta é nula, então apagamos ela manualmente


    for i in range(0,len(paginas)):
        if not bool(paginas[i]):
            paginas[i] = lastTrue
        else:
            lastTrue = paginas[i]

    x = 0
    nomeLivroTratado = corrigeNome(filename)
    while x != 500:
        nomeLivro.append(nomeLivroTratado)
        x += 1

    respostas = limpaTexto(respostas)
    respostas = limpaRespostas(respostas)
    perguntas = limpaTexto(perguntas)
    perguntas = limpaPergunta(perguntas)



    conjunto = [perguntas,respostas,paginas,nomeLivro]
    filepath = os.path.abspath(os.path.join(basepath, "..", "txt", "500pr_procTxt_" + filename + ".txt"))
    with open(filepath, 'wb') as fp:
       pickle.dump(conjunto, fp)


def run(perguntaUser, livro):
    if(livro) == "todos":
        return runAll(perguntaUser)
    filepath = os.path.abspath(os.path.join(basepath, "..", "txt", "500pr_procTxt_" + livro + ".txt"))
    with open(filepath, 'rb') as file:
        lista = pickle.load(file)
    perguntas = lista[0]
    respostas = lista[1]
    paginas = lista[2]
    nomeLivro = lista[3]

    listaRatio = []
    i = 0

    for index, pergunta in enumerate(perguntas):
        listaRatio.append([ i , checkRatio(perguntaUser, pergunta)])
        i += 1

    sortedList = sorted(listaRatio, key=lambda l: l[1],reverse=True)[:3]

    top3 = {"0": {"pergunta": perguntas[sortedList[0][0]], "resposta": respostas[sortedList[0][0]],
                  "pagina": paginas[sortedList[0][0]], "ratio": sortedList[0][1], "nomeLivro":nomeLivro[sortedList[0][0]]},
            "1": {"pergunta": perguntas[sortedList[1][0]], "resposta": respostas[sortedList[1][0]],
                  "pagina": paginas[sortedList[1][0]], "ratio": sortedList[1][1], "nomeLivro":nomeLivro[sortedList[0][0]]},
            "2": {"pergunta": perguntas[sortedList[2][0]], "resposta": respostas[sortedList[2][0]],
                  "pagina": paginas[sortedList[2][0]], "ratio": sortedList[2][1], "nomeLivro":nomeLivro[sortedList[0][0]]}
            }

    #0 = pergunta similar, 1 = resposta da pergunta, 2 = pagina encontrada, 3 = ratio da resposta, 4 nome do livro
    return top3

def runAll(perguntaUser):
    lista = []
    listaLivros = getListaLivros()
    newTop3 = {}
    for i in range(0,len(listaLivros)):
        top3 = (run(perguntaUser, listaLivros[i][0]))
        for x in range(0,3):
            lista.append(top3[str(x)])
    sortedList = sorted(lista, key=lambda l: l["ratio"], reverse=True)[:3]
    for i in range(0,3):
        newTop3[str(i)] = sortedList[i]
    return newTop3

def checkRatio(str1, str2):
    bestRatio = 0
    ratios = [fuzz.ratio(str1, str2), fuzz.partial_ratio(str1, str2), fuzz.token_sort_ratio(str1, str2),
              fuzz.token_set_ratio(str1, str2)]
    for ratio in ratios:
        if ratio > bestRatio:
            if (len(str1) <= 5) or (len(str2) <=5):
                bestRatio = 25
            else:
                bestRatio = ratio
    return bestRatio


def limpaTexto(listaentrada):
    rgxPage = re.compile('500pr_pgnumber\w{3}')
    listasaida = []
    for item in listaentrada:
        if isinstance(item,str):
            listasaida.append(re.sub(rgxPage, '', item))
        elif isinstance(item,list):
            try:
                listasaida.append(re.sub(rgxPage, '', item[0]))
            except IndexError:
                pass
    return listasaida


def limpaPergunta(listaentrada):
    listasaida = []
    for item in listaentrada:
        try:
            if isinstance(item, str):
                listasaida.append(item.lstrip('0123456789.- '))
            elif isinstance(item, list):
                listasaida.append(item[0].lstrip('0123456789.- '))
        except IndexError:
            pass
    return listasaida

def limpaRespostas(listaentrada):
    listasaida = []
    for item in listaentrada:
        try:
            if isinstance(item, str):
                listasaida.append(item.lstrip('?'))
            elif isinstance(item, list):
                listasaida.append(item[0].lstrip('?'))
        except IndexError:
            pass
    return listasaida

def corrigeNome(nomeLivro):
    lista = getListaLivros()
    for dadosLivro in lista:
        if nomeLivro == dadosLivro[0]:
            nomeLivroTratado = dadosLivro[5]
    return nomeLivroTratado