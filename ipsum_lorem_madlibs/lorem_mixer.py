from random import randint
#retorna um int in range

prog_words = [
    'Pythonic', 'Sharp', 'Javascript', 'Fortran', 'Oh Java',
    'Pascal', 'So Basic', 'PlusPlus', 'Dotnet', 'Nosql',
    'Ruby', 'Rails', 'React', 'ECMA'
]
#essas palavras serão injetadas aleatoriamente dentro do lorem

def mixer(word):
#essa palavra recebida vem o lorem_vanila.txt
    aleatorio = randint(0, len(prog_words)-1)
    #o randint precisa de um range e inclui os 2 endpoints
    #por isso o -1 pro index ser válido
    return f'{word} {prog_words[aleatorio]}'
    #retorna 1 palavra original + 1 palavra aleatoria do
    #prog_words pareado

paragrafos = int(input('Quantos paragrafos você quer: '))
#vou pegar esse valor numérico para saber quantos
#paragrafos/linhas imprimir no final

with open('lorem_vanila.txt') as original:
#abre o arquivo original
    palavras = original.read().split()
    #palavras será uma lista cujos elementos são as palvras
    #do lorem_vanila
    #print(palavras[0])

for n in range(paragrafos):
#para um valor n dentro do range do nº paragrafos informado
    prog_texto = list(map(mixer, palavras))
    #o retorno disso é uma lista onde cada elemento é o
    #conjunto retornado da função mixer
    #print(prog_texto)
    with open('lorem_prog.txt', 'a') as misturado:
    #abre o arquivo que vai ser escrito e AMENDS IT
        misturado.write(' '.join(prog_texto) + '\n\n')
        #em misturado escreva cada elemento do prog_texto
        #separados por ESPAÇO
        #o resultado é um lista onde cada elemento é um
        #paragrafo formado pelos retornos da mixer