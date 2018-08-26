import re
from core.functions import *
from core.data import *

def regexTest():
	result = run("qual a melhor epoca", "algodao")
	print(result['0']['pergunta'][0])
	rgxPage = re.compile('500pr_pgnumber\w{3}')
	end = re.sub(rgxPage,'', result['0']['pergunta'][0])
	print(end)

print(run("qual a melhor epoca", "abacaxi"))
#print(core.functions.run("testando testes","amendoim"))

