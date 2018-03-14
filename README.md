# Sis500
(Now with English README, check below!)

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

-----------------------------------------------------------------------------------------------------
# Sis500
Program that uses Approximate String Matching (ASM) to search answers to asked questions by the user inside a collection of books related to general farming subjects, such as livestock, cotton, beans, etc.
The organization responsible for the books is EMBRAPA, and the collection is named "500 Perguntas, 500 Respostas"(500 Questions, 500 Answers).
Using Approximate String Matching, Text Mining, and Flask, we built this website which grabs the specific question the user has and looks for the best answer inside the books.

LINKS:
Site: http://bk201.pythonanywhere.com
Books : http://mais500p500r.sct.embrapa.br/view/index.php
EMBRAPA's International Site: https://www.embrapa.br/en/international

Collaborators:
Lucas Baum Pereira - @dekken201
Luciano Latocheski - @latocheski
Prof. Me. Edie Correia Santana

Used libraries/tools and their links:

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
