from src.read_files import read_file
import math


def index_files(files: list) -> dict:
    """
    Gera o indice invertido e uma representação sobre os documentos

    args:
        files -> list: lista de dicionários {'caminho':'caminho/arquivo.txt', 'nome': 'arquivo.txt'}
    returns:
        {"index": {"termo1":{'df': 1, 'idf': 0, 'docs': {'arquivo.txt': 1}}}, "docs": {'termos':{'termo1':{'freq':1}}}}
    """
    qtd_doc = len(files)
    indice = {}
    documentos = {}
    for fp in files:
        words = read_file(fp['caminho'])
        for word in words:
            if word in indice:
                if fp['nome'] in indice[word]['docs']:
                    indice[word]['docs'][fp['nome']] += 1
                else:
                    indice[word]['docs'][fp['nome']] = 1
                    indice[word]['df'] += 1
            else:
                indice[word] = {'df': 1, 'idf': 0, 'docs': {fp['nome']: 1}}
            if fp['nome'] in documentos:
                if word in documentos[fp['nome']]['termos']:
                    documentos[fp['nome']]['termos'][word]['freq'] += 1
                    if documentos[fp['nome']]['termos'][word]['freq'] > documentos[fp['nome']]['max']:
                        documentos[fp['nome']]['max'] = documentos[fp['nome']]['termos'][word]['freq']
                else:
                    documentos[fp['nome']]['termos'][word] = {'freq': 1}
            else:
                documentos[fp['nome']] = {'max': 1,'termos': {word: {'freq': 1}}}
    sorted_index = {}
    for i in sorted(indice):
        indice[i]['idf'] = math.log(qtd_doc/indice[i]['df'], 10)
        sorted_index[i] = indice[i]
    return {"index": sorted_index, "docs": documentos}


def print_index(indice: dict):
    print("termo  |  df  |  idf  |  docs")
    for i in indice:
        print(
            f"{i}  |  {indice[i]['df']}  |  {indice[i]['idf']}  |  {indice[i]['docs']}")
