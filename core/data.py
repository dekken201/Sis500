#0 = nome do livro, 1 = indice de inicio do getAnswers,2, indice final,3 = pergunta zero, 4 = modo de gravação de txt
#5 = nome livro correto
listaLivros = \
	[
	["abacaxi", 16, 194, "A falta de chuva prejudica o abacaxizeiro", "w", "Abacaxi"],
	["algodao", 17, 266, "Qual a origem mais provável do algodoeiro", "w", "Algodão"],
	["amendoim", 17, 240, "Quais os fatores climáticos mais importantes para o crescimento da planta e o desenvolvimento do amendoim", "wb", "Amendoim"],
	["arroz", 17, 246,  "Quais são os elementos climáticos que mais influenciam a produtividade do arroz de terras altas", "w", "Arroz"],
	["banana", 13, 199,  "Onde se originou a bananeira e quais espécies participaram da sua evolução", "w", "Banana"],
	["bufalos", 13, 161, "O que são búfalos domésticos e qual sua origem", "w", "Búfalos"],
	["caju", 19, 249,  "Qual é a origem do cajueiro", "wb", "Caju"],
	["caprinos_ovinos_corte", 17, 242,  "Saber criar caprinos e ovinos de corte é suficiente para ganhar dinheiro", "w", "Caprinos e Ovinos de Corte"],
	["citros", 16, 212, "Como está classificado o gênero citros", "wb", "Citros"],
	["feijao", 17, 247,  "O que é um feijão", "wb", "Feijão"],
	["fruticultura_irrigada", 20, 274,  "Como o clima afeta a produção de plantas", "wb", "Fruticultura Irrigada"],
	["gado_corte",14, 253,  "Como deve ser o manejo do rebanho de cria na época de nascimentos", "w", "Gado de Corte"],
	["gado_corte_pantanal",16, 256,  "Quando começou a pecuária de corte no Pantanal", "w", "Gado de Corte do Pantanal"],
	["gado_leite", 14, 297, "Quando iniciar os cuidados com os bezerros", "wb", "Gado de Leite"],
	["geotecnologia_geoinformacao",17, 249, "O que é um satélite artificial", "wb", "Geotecnologia e Geoinformação"],
	["gergelim", 19, 210, "Qual é o local de origem do gergelim", "wb", "Gergelim"],
	["hortas", 18, 237, "O que são hortaliças", "wb", "Hortas"],
	["integracao_lavoura_pecuaria_floresta", 23, 393,  "O que é integração lavoura-pecuária-floresta (ILPF)", "wb", "Integração Lavoura-Pecuária-Floresta"],
	["maca", 12, 225, "Qual é o local de origem da macieira", "wb", "Maçã"],
	["mamao", 17, 171, "Quais as características da família Caricaceae", "w", "Mamão"],
	["mamona", 17, 249, "Como escolher uma área adequada para cultivar mamona", "wb", "Mamona"],
	["mandioca", 17, 177, "A que ordem, família, gênero e espécie pertence a mandioca", "w", "Mandioca"],
	["manga", 17, 185, "Qual a classificação botânica da mangueira", "w", "Manga"],
	["maracuja", 17, 341, "Qual a origem da palavra maracujá", "wb", "Maracuja"],
	["milho", 18, 327, "Como o clima influencia a cultura do milho", "wb", "Milho"],
	["ovinos", 15, 159, "Como uma associação de pequenos criadores de ovinos, dos quais alguns também criam caprinos, pode obter recursos financeiros e apoio técnico", "w", "Ovinos"],
	["pequenas_frutas", 13, 183, "Por que as pequenas frutas recebem essa denominação", "w", "Pequenas Frutas"],
	["pera",19, 231, "Qual é o centro de origem da pereira", "wb", "Pêra"],
	["pesca_piscicultura_pantanal", 17, 189, "O que são recursos pesqueiros", "w", "Pesca e Piscicultura do Pantanal"],
	["poscolheita_hortalicas", 15, 252, "Produzir hortaliças é um bom negócio", "wb", "Póscolheita de Hortaliças"],
	["producao_organica_hortalicas", 18, 299, "O que é agroecologia", "w", "Produção Orgânica de Hortaliças"],
	["sistema_plantio_direto", 17, 249, "O que são sistemas conservacionistas de manejo do solo", "w", "Sistema de Plantio Direto"],
	["sorgo", 17, 324, "Como saber a época mais indicada para o plantio de sorgo granífero", "w", "Sorgo"],
	["suinos", 17, 244, "Qual a diferença entre granja de suínos e sistema de produção de suínos", "w", "Suínos"],
	["trigo", 17, 309, "Qual é a origem do trigo", "w", "Trigo"],
	["uva", 17, 203, "Quais são os métodos usados no melhoramento genético da videira", "w", "Uva"]
	]


def getListaLivros():
	return listaLivros

