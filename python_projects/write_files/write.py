with open('write.txt', 'w') as write_file:
    #'w' stands for WRITE
    write_file.write('Hey there ninjas, python is awesome')
    # .write espera receber como arg 1 linha de texto
    # write_file.write('\nI love it so much, I dream in python')

with open('write.txt', 'a') as write_file:
    #'a' stands for AMENDS, ele adiciona a frase ao arquivo
    #se fosse 'w' aqui, iria sobrescrever a partir da 1ª linha
    #\n é uma quebra de linha
    write_file.write('\nI love it so much, I dream in python')

quotes = [
    '\nI can resist everything except temptation',
    '\nWe are all in the gutter, but some of us are looking at the stars',
    '\nAlways forgive your enemies - nothing annoys them so much'
]

with open('write.txt', 'a') as write_file:
    # .writelines() espera receber algum tipo de lista como arg
    write_file.writelines(quotes)