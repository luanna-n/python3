import urllib.request

def dl_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    #esse full_path é o caminho ../img/
    # + o nome do arquivo ../img/dog
    # + o nome da extensão ../img/dog.jpg
    #poderia ser .png tranquilamente
    urllib.request.urlretrieve(url, full_path)

url = input('Enter image URL to download: ')
file_name = input('Enter file name to save as: ')

dl_jpg(url, '', file_name)
""" 
Recebe a url que o user deu, 
- o caminho para salvar o arquivo, que será nesta pasta mesmo
- mas poderia ser em outra, por exemplo:
    ../beecrowd/
- e o nome que o user deu para o arquivo
"""