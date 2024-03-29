from src.pre_process import remove_stop_words
import math
from tabulate import tabulate



def calculate_similarity(index_docs: dict, busca: str) -> dict:
    """
    Calcula a similaridade entre os termos de entrada da busca com relação aos documentos indexados
    args:
        index_docs:dict 
            {"index": {"termo1":{'df': 1, 'idf': 0, 'docs': {'arquivo.txt': 1}}}, "docs": {'termos':{'termo1':{'freq':1}}}}
        busca:str termos da busca
    returns:
        {'documento1':'similaridade', 'documento2': 'similaridade'}
    """
    consulta = {}
    documentos = {}
    words = remove_stop_words(busca)
    f_maximo = 1
    alfa = 0.5
    for word in words:
        if word in consulta:
            consulta[word]['freq'] += 1
            if consulta[word]['freq'] > f_maximo:
                f_maximo = consulta[word]['freq']
        else:
            consulta[word] = {'freq': 1, "w": 0, "quad": 0}
    soma = 0
    for c in consulta:
        idf = 0
        if c in index_docs['index']:
            idf = index_docs['index'][c]['idf']
        consulta[c]['w'] = (alfa + (((1-alfa)*consulta[c]['freq'])/f_maximo))*idf
        consulta[c]['quad'] = consulta[c]['w']**2
        if c in index_docs['index']:
            for doc in index_docs['index'][c]['docs']:
                if doc in documentos:
                    documentos[doc] += index_docs['docs'][doc]['termos'][c]['tfidf'] * \
                        consulta[c]['w']
                else:
                    documentos[doc] = index_docs['docs'][doc]['termos'][c]['tfidf'] * \
                        consulta[c]['w']
        soma += consulta[c]['quad']
    consulta['raiz'] = math.sqrt(soma)
    consulta['freq_max'] = f_maximo
    similaritys = {}
   
    for dc in documentos:
        similaritys[dc] = documentos[dc] / \
            (index_docs['docs'][dc]['raiz']*consulta['raiz'])
    return dict(sorted(similaritys.items(), key=lambda item: item[1],reverse=True))


def print_similaritys(similaritys: dict)->None:
    """
    imprime uma tabela de similaridade da consulta com os documentos

    args:
        similaritys:dict 
            {'documento1':'similaridade', 'documento2': 'similaridade'}
    """

    if len(similaritys) > 0:
        print("\nSimilaridades:\n")
        print(tabulate([similaritys.values()],
                    headers=list(similaritys.keys())))
        print("\nRanking:\n")
        print(tabulate([list(similaritys.keys())],headers=[x for x in range(0, len(similaritys.keys()))]))
    else:
        print("A consulta não retornou documentos relevantes")