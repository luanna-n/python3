from random import shuffle
#esse metodo devolve o input fora da ordem original

def embaralha(palavra):
#função que vai embaralhar as palavras
    anagrama = list(palavra)
    #anagrama é uma lista formada pelas letras de cada palavra
    shuffle(anagrama)
    #embaralha as letras
    return "".join(anagrama)
    #join concatena listas

palavras = ['acerola', 'caju', 'graviola']
#essa é a lista original, de onde sairão as palavras
#que serão embaralhadas
anagramas = [ ]
#essa é lista com as palavras embaralhadas

for palavra in palavras:
#para cada palavra na lista palavras
    anagramas.append(embaralha(palavra))
    #jogue dentro da lista anagramas o retorno da função
    #embaralha para aquela palavra
print(anagramas)
#quando o loop for acabar, ele imprime a lista com cada
#uma das palavras devidamente embaralhadas e na ordem original


#fazer o for usando o map
#new_list = map(function, dados)
print(map(embaralha, palavras))
#exibe um map object
print(list(map(embaralha, palavras)))
#mesmo resultado do for, type casted into a list

#list comprehension
ana_comp = [ embaralha(palavra) for palavra in palavras ]
print(ana_comp)