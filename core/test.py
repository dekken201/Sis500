import re
from core.functions import *
from core.data import *

def regexTest():
    result = run("qual a melhor epoca", "algodao")
    print(result['0']['pergunta'][0])
    rgxPage = re.compile('500pr_pgnumber\w{3}')
    end = re.sub(rgxPage,'', result['0']['pergunta'][0])
    print(end)

def perguntaTest():
    result1 = run("qual a melhor epoca de plantio", "algodao")
    result2 = run("qual a melhor epoca para realizar a lavagem", "algodao")
    result3 = run("quais são os limites de radiacao solar", "abacaxi")
    r1 = result1['0']['pergunta']
    r2 = result2['0']['pergunta']
    r3 = result3['0']['pergunta']
    print(r1)
    print(r1.lstrip('0123456789.- '))
    print(r2)
    print(r2.lstrip('0123456789.- '))
    print(r3)
    print(r3.lstrip('0123456789.- '))


#print(run("qual a melhor epoca", "abacaxi"))
#print(core.functions.run("testando testes","amendoim"))
getAnswers(lista)
