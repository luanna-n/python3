""" ipsum = open('lorem.txt')

#le o arquivo por linhas até o final
for line in ipsum:
    print(line)

#retorna para o inicio do arquivo
ipsum.seek(0)

#le o arquivo e o retorna como [] cada linha separada por virgula
lines = ipsum.readlines()
print(lines)

#comeca a ler o arquivo no item 50 e lê 100 itens a partir dele
ipsum.seek(50)
file_text = ipsum.read(100)
print(file_text)

#fecha o arquivo para não comprometer o processamento
ipsum.close()
 """

#filtrar a lista para remover as linhas com dados que não
#são uteis
def remove(line):
    #retorna if TRUE < is not inside that line of data
    return ">" not in line

#forma melhor de ler, sem ter que preocupar com close()
with open('dna.txt') as dna_file:
    #preciso armazenar meus dados
    lines = dna_file.readlines()
    #agora vou filtrar esses dados usando a função que
    #criei acima, typecast it into a list and print
    #print(list(filter(remove, lines)))

    #tambem posso armazenar separadamente e imprimir
    #pelo index, onde cada item é 1 linha de código
    itens = list(filter(remove, lines))
    print(itens[5])

#para fechar a conexão, basta sair do bloco