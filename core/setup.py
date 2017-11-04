#ALGUMAS PERGUNTAS ESTÃO DESCONFIGURADAS. O INDICE 505 É A PERGUNTA nº 500
#TO DO!
#pensar em uma forma de sanitizar as perguntas e tirar os espaços/pagenumbers que ficam atrapalhando
#mudar regex das páginas para sub em vez de findall
from core.functions import *


#COMPILAÇÃO DO TEXTO:
#getText("abacaxi",16) #OK
#getText("algodao",16) #OK
#getText("amendoim",16) #wb OK
#getText("arroz",16)
#getText("banana",16)
#getText("bufalos",16)
#getText("caju",18) #wb
#getText("caprinos_ovinos_corte",16)
#getText("citros",16) #wb
#getText("feijao",16) #wb
#getText("fruticultura_irrigada",20) #wb
#getText("gado_corte",18)
#getText("gado_corte_pantanal",17)
#getText("gado_leite",20) #wb
#getText("geotecnologia_geoinformacao",16)
#getText("gergelim",18) #wb
#getText("hortas",17) #wb
#getText("integracao_lavoura_pecuaria_floresta",22) #wb
#getText("maca",16) #wb
#getText("mamao",16)
#getText("mamona",16) #wb
#getText("mandioca",16)
#getText("manga",16)
#getText("maracuja",16) #wb
#getText("milho",20) #wb
#getText("ovinos",14)
#getText("pequenas_frutas",16)
#getText("pera",16) #wb
#getText("pesca_piscicultura_pantanal",16)
#getText("poscolheita_hortalicas",14) #wb
#getText("producao_organica_hortalicas",18)
#getText("ricino",0) #EM ESPANHOL
#getText("sistema_plantio_direto",16)
#getText("sorgo",16)
#getText("suinos",16)
#getText("trigo",16)
#getText("uva",16)


#COMPILAÇÃO DAS PERGUNTAS:
#getAnswers("abacaxi", "A falta de chuva prejudica o abacaxizeiro") #OK
#getAnswers("algodao", "Qual a origem mais provável do algodoeiro") #OK
#getAnswers("amendoim", "Quais os fatores climáticos mais importantes para o crescimento da planta e o desenvolvimento do amendoim") #OK
#getAnswers("arroz", "Quais são os elementos climáticos que mais influenciam a produtividade do arroz de terras altas")
#getAnswers("banana", "Onde se originou a bananeira e quais espécies participaram da sua evolução")
#getAnswers("bufalos", "O que são búfalos domésticos e qual sua origem")
#getAnswers("caju", "Qual é a origem do cajueiro")
#getAnswers("caprinos_ovinos_corte", "Saber criar caprinos e ovinos de corte é suficiente para ganhar dinheiro")
#getAnswers("citros", "Como está classificado o gênero citros")
#getAnswers("feijao", "O que é um feijão")
#getAnswers("fruticultura_irrigada", "Como o clima afeta a produção de plantas")
#getAnswers("gado_corte", "Como deve ser o manejo do rebanho de cria na época de nascimentos")
#getAnswers("gado_corte_pantanal", "Quando começou a pecuária de corte no Pantanal")
#getAnswers("gado_leite", "Quando iniciar os cuidados com os bezerros")
#getAnswers("geotecnologia_geoinformacao", "O que é um satélite artificial")
#getAnswers("gergelim", "Qual é o local de origem do gergelim")
#getAnswers("hortas", "O que são hortaliças")
#getAnswers("integracao_lavoura_pecuaria_floresta", "O que é integração lavoura-pecuária-floresta (ILPF)")
#getAnswers("maca", "Qual é o local de origem da macieira")
#getAnswers("mamao", "Quais as características da família Caricaceae")
#getAnswers("mamona", "Como escolher uma área adequada para cultivar mamona")
#getAnswers("mandioca", "A que ordem, família, gênero e espécie pertence a mandioca")
#getAnswers("manga", "Qual a classificação botânica da mangueira")
#getAnswers("maracuja", "Qual a origem da palavra maracujá")
#getAnswers("milho", "Como o clima influencia a cultura do milho")
#getAnswers("ovinos", "Como uma associação de pequenos criadores de ovinos, dos quais alguns também criam caprinos, pode obter recursos financeiros e apoio técnico?")
#getAnswers("pequenas_frutas", "Por que as pequenas frutas recebem essa denominação")
#getAnswers("pera", "Qual é o centro de origem da pereira")
#getAnswers("pesca_piscicultura_pantanal", "O que são recursos pesqueiros")
#getAnswers("poscolheita_hortalicas", "Produzir hortaliças é um bom negócio")
#getAnswers("producao_organica_hortalicas", "O que é agroecologia")
#getAnswers("ricino", "XXXXXXXXXXXXXXXXXXXXXXX") #EM ESPANHOL
#getAnswers("sistema_plantio_direto", "O que são sistemas conservacionistas de manejo do solo")
#getAnswers("sorgo", "Como saber a época mais indicada para o plantio de sorgo granífero")
#getAnswers("suinos", "Qual a diferença entre granja de suínos e sistema de produção de suínos")
#getAnswers("trigo", "Qual é a origem do trigo")
#getAnswers("uva", "Quais são os métodos usados no melhoramento genético da videira")


#RODAR PROGRAMA:
#print(run("a falta de chuva prejudica o abacaxi","abacaxi"))
#print(run("testando testes","amendoim"))


