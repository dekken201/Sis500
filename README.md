# Sis500
Programa que usa Correspondência Aproximada de Strings(CAS) para buscar respostas de perguntas feitas pelo usuário em coletâneas pré-definidas.
Utilizando a coletânea 500 Perguntas, 500 Respostas da EMBRAPA , realizamos a mineração do texto dos PDFs disponibilizados gratuitamente, e utilizando a CAS, mais precisamente o algoritmo da Distância de Levenshtein, implementada com a biblioteca FuzzyWuzzy, comparamos as perguntas do usuário com a base de dados do livro, que retorna os conteúdos relacionados ao usuário.
Para a implementação web, foi utilizado o framework Flask, e o projeto está hospedado no PythonAnywhere.

LINKS:
Site: http://bk201.pythonanywhere.com
Coletânea EMBRAPA : http://mais500p500r.sct.embrapa.br/view/index.php

Colaboradores:
Lucas Baum Pereira - @dekken201
Luciano Latocheski - @latocheski
Prof. Me. Edie Correia Santana

Bibliotecas utilizadas e seus respectivos links:

Flask 
https://github.com/pallets/flask

FuzzyWuzzy(Seatgeek) 
https://github.com/seatgeek/fuzzywuzzy /
http://chairnerd.seatgeek.com/fuzzywuzzy-fuzzy-string-matching-in-python/

pdfminer.six(pdfminer para Python3) 
https://github.com/euske/pdfminer /
https://github.com/pdfminer/pdfminer.six

PythonAnywhere
https://www.pythonanywhere.com/
