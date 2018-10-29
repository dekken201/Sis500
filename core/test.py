# -*- coding: utf-8 -*-
import re
from core.functions import *
from core.data import *
import re, pickle, os

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
    print("["+stringteste.split("?",)[0]+"]")
    print("["+stringteste.split("?")[1]+"]")
    print("[" + stringteste.split("?")[2] + "]")
    print(re.split(rgx, stringteste))

def todosTest():
    filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "txt", "500pr_procTxt_" + "todos" + ".txt"))
    with open(filepath, 'rb') as file:
        lista = pickle.load(file)
        print(lista[0])
        print(len(lista[0]))


def runTest():
    lista = []
    newTop3 = {}
    test1 = run("plantio do algodao 2222222","abacaxi")
    test2 = run("plantio do algodao asadsd","algodao")
    for i in range(0,3):
        lista.append(test1[str(i)])
        pass
    for i in range(0,3):
        lista.append(test2[str(i)])
    sortedList = sorted(lista, key=lambda l: l["ratio"], reverse=True)[:3]
    for i in range(0,3):
        newTop3[str(i)] = sortedList[i]
    print(newTop3)

#runTest()

print (run("quanto ao plantio do algodao","todos"))