from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk import download
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

def __get_files_path() -> list:
    """
    obtem uma lista dos arquivos
    """
    files = []
    inner_folders = __get_folder('arquivos')
    for folder in inner_folders:
        files += __get_ful_path(folder)
    return files

def __download_stop_words()->None:
    """
    Ação pré requisito da biblioteca
    baixar as stopwords
    """
    download('stopwords')
    download('punkt')

def __remove_stop_words(text:str)->str:
    
    stop_wordsPort = set(stopwords.words('portuguese')) 
    word_tokens = word_tokenize(text) 
    filtered_sentence = [w for w in word_tokens if not w in stop_wordsPort] 
    return filtered_sentence

def read_files():
    files = __get_files_path()
    __download_stop_words()
    for fp in files:
        with open(fp['caminho'], 'r') as r:
            lista = __remove_stop_words(r.readlines())
    #with open()


    
    