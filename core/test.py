#ALGUMAS PERGUNTAS ESTÃO DESCONFIGURADAS. O INDICE 505 É A PERGUNTA nº 500
#TO DO!
#pensar em uma forma de sanitizar as perguntas e tirar os espaços/pagenumbers que ficam atrapalhando
#mudar regex das páginas para sub em vez de findall
from core.functions import *

#COMPILAÇÃO DO TEXTO:
#getText("500pr","500pr_txt_algodao")

#COMPILAÇÃO DAS PERGUNTAS:
getAnswers("500pr_txt_algodao")

#RODAR PROGRAMA:
print(run("origem algodao cara","algodao"))


