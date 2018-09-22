# -*- coding: utf-8 -*-
import re
from core.functions import *
from core.data import *
import re

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

def splitTest():
    rgx = '(?=\?\n)'

    stringteste = """A tolerância à seca desse acesso de espécie silvestre pode
ser introgredida no amendoim cultivado? Qual a importância
desse estudo para o Nordeste?

Sim. Para o melhoramento do amendoim cultivado, um trabalho
dessa natureza torna-se importante devido ao aproveitamento """
    #print("["+stringteste.split("?",)[0]+"]")
    #print("["+stringteste.split("?")[1]+"]")
    #print("[" + stringteste.split("?")[2] + "]")
    print(re.split(rgx, stringteste))

#splitTest()

#print(run("a tolerancia a seca desse", "amendoim"))
#print(core.functions.run("testando testes","amendoim"))
#getAnswers(lista)

