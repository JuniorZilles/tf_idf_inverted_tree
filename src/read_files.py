from src.pre_process import remove_stop_words
import os


def __get_folder(pasta:str)->list:
    """
    obtem as pastas de dentro do diretorio

    args:
        pasta: nome da pasta principal
    
    return
        lista das subpastas
    """
    lista = []
    for nome in os.listdir(pasta):
        lista.append(os.path.join(pasta, nome))
    return lista

def __get_ful_path(pasta:str)->list:
    """
    obtem os arquivos de dentro de um diretorio

    args:
        pasta: nome da pasta
    
    return
        lista contendo um dicionário com o caminho e o nome
    """
    lista = []
    for nome in os.listdir(pasta):
        lista.append({"caminho": os.path.join(pasta, nome), "nome":nome.lower()})
    return lista

def get_files_path() -> list:
    """
    obtem uma lista dos arquivos

    returns:
        lista de dicionários {'caminho':'caminho/arquivo.txt', 'nome': 'arquivo.txt'}
    """
    files = []
    inner_folders = __get_folder('arquivos')
    for folder in inner_folders:
        files += __get_ful_path(folder)
    return files

def read_file(caminho)->list:
    words = []
    with open(caminho, 'r', encoding='UTF-8') as r:
        words = remove_stop_words(r.read())
    return words



   



    
    