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
def getText(pdfname,pageZero): #Função que extrai o texto do pdf, usando os parâmetros padrão da biblioteca pdfminer
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'latin-1'
    laparams = LAParams()
    path = "C:/Users/Luke/Documents/Prog/Python/Sis500/pdf/500pr/500pr_"+pdfname+".pdf"
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb') #Pega o arquivo do pdf no caminho especificado
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    #Roda um loop, usando todos os atributos anteriores, interpretando o pdf por página e realizando a conversão
    for pagenumber, page in enumerate(PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True)):
        if pagenumber < pageZero -1: #Pula as primeiras 16 páginas, que não possuem nenhuma pergunta/resposta
            pass
        else:
            if pagenumber >= 100:
                retstr.write("\n 500pr_pgnumber" + str(pagenumber) +"\n")
            else:
                retstr.write("\n 500pr_pgnumber0" + str(pagenumber) +"\n")
            interpreter.process_page(page)


    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()

    try:
        with open("C:/Users/Luke/Documents/Prog/Python/Sis500/txt/test/500pr_txt_"+pdfname+".txt", "w") as textFile:
            textFile.write(text)
    except UnicodeEncodeError:
        with open("C:/Users/Luke/Documents/Prog/Python/Sis500/txt/test/500pr_txt_"+pdfname+".txt", "w",encoding='utf-8') as textFile:
            textFile.write(text)



def getAnswers(filename,perguntaZero): #Função que separa as perguntas e respostas do texto minerado do pdf
    filepath = "C:/Users/Luke/Documents/Prog/Python/Sis500/txt/test/500pr_txt_" + filename+ ".txt"

    respostas = []
    perguntas = []
    paginas = []
    try:
        file = open(filepath,"r")#Abre o arquivo de texto
        file = file.read()
    except UnicodeDecodeError:
        file = open(filepath, "r",encoding='utf-8')  # Abre o arquivo de texto
        file = file.read()

    rgx = re.compile('(?<=\.)[^.]*$')  # Compilação do regex a ser utilizado no loop
    rgxPage = re.compile('(?<=500pr_pgnumber)\w{3}')

    i = 0
    while True:
        try:
            splitString = file.split("?")[i]
        except IndexError:
            break

        respostas.append(splitString) #As duas listas recebem a mesma string separadas no "?"
        perguntas.append(" ".join(splitString.split())) #Retira grande parte do espaço em branco e desnecessário da string perguntas
        paginas.append(splitString)

        respostas[i] = re.sub(rgx,'', respostas[i]) #Porém uma pega o regex sem a pergunta(a resposta)
        perguntas[i] = rgx.findall(perguntas[i]) #e a outra pega o regex que só dá match na pergunta(a pergunta)
        paginas[i] = rgxPage.findall(splitString)

        i += 1


    perguntas[0] = perguntaZero #Por motivos específicos, o código não consegue pegar a primeira pergunta, então temos que colocá-la manualmente
    respostas.pop(0) #Pelo mesmo motivo, a primeira resposta é nula, então apagamos ela manualmente

    print (perguntas[0])
    print(respostas[0])

    for i in range(0,len(paginas)):
        if not bool(paginas[i]):
            paginas[i] = lastTrue
        else:
            lastTrue = paginas[i]

    conjunto = [perguntas,respostas,paginas]
    filepath = "C:/Users/Luke/Documents/Prog/Python/Sis500/txt/test/500pr_procTxt_" + filename + ".txt"
    with open(filepath, 'wb') as fp:
       pickle.dump(conjunto, fp)

def run(perguntaUser, livro):
    filepath = "C:/Users/Luke/Documents/Prog/Python/Sis500/txt/test/500pr_procTxt_"+ livro + ".txt"
    with open(filepath, 'rb') as file:
        lista = pickle.load(file)

    perguntas = lista[0]
    respostas = lista[1]
    paginas = lista[2]

    bestMatchIndex = 0
    bestRatio = 0

    for index, pergunta in enumerate(perguntas):
        ratio = checkRatio(perguntaUser, pergunta)
        if ratio > bestRatio:
            bestMatchIndex = index
            bestRatio = ratio

    answer = [perguntas[bestMatchIndex], respostas[bestMatchIndex], paginas[bestMatchIndex], bestRatio]
    #0 = pergunta similar, 1 = resposta da pergunta, 2 = pagina encontrada, 3 = ratio da resposta

    return stringBuilder(answer)

def stringBuilder(answer):
    pergunta = answer[0]
    resposta = answer[1]
    pagina = answer[2]
    ratio = answer[3]

    return "Pergunta relacionada:\n"+ str(pergunta) +"\nResposta: "+ str(resposta) +"\nPágina da pergunta: "+ str(pagina) +"\nProximidade: "+str(ratio)

def checkRatio(str1, str2):
    bestRatio = 0
    ratios = [fuzz.ratio(str1, str2), fuzz.partial_ratio(str1, str2), fuzz.token_sort_ratio(str1, str2),
              fuzz.token_set_ratio(str1, str2)]
    for ratio in ratios:
        if ratio > bestRatio:
            bestRatio = ratio
    return bestRatio

