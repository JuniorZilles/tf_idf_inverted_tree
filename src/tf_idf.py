import math
from tabulate import tabulate

def tf_idf_documents(index_docs: dict):
    """
    Gera a representação do modelo vetorial calculando o tfidf de cada termo nos documentos
    
    args:
        index_docs:dict 
            {"index": {"termo1":{'df': 1, 'idf': 0, 'docs': {'arquivo.txt': 1}}}, "docs": {'termos':{'termo1':{'freq':1}}}}
    """
    for doc in index_docs['docs']:
        freq_maxima = index_docs['docs'][doc]['max']
        soma = 0
        for termo in index_docs['docs'][doc]['termos']:
            index_docs['docs'][doc]['termos'][termo]['tfidf'] = (
                index_docs['docs'][doc]['termos'][termo]['freq']/freq_maxima)*index_docs['index'][termo]['idf']
            #index_docs['docs'][doc]['tfidf'] += index_docs['docs'][doc]['termos'][termo]['tfidf']
            index_docs['docs'][doc]['termos'][termo]['quad'] = index_docs['docs'][doc]['termos'][termo]['tfidf']**2
            soma += index_docs['docs'][doc]['termos'][termo]['quad']
        index_docs['docs'][doc]['raiz'] = math.sqrt(soma)


def print_tf_idf(index_docs: dict):
    """
    Gera a tabela contendo a representação do modelo vetorial

    args:
        index_docs:dict 
            {"index": {"termo1":{'df': 1, 'idf': 0, 'docs': {'arquivo.txt': 1}}}, "docs": {'termos':{'termo1':{'freq':1}}}}
    """
    lenght_t = len(index_docs['index'])+1
    lista = [None]*lenght_t
    ind_t = 1
    for doc in index_docs['docs']:
        if lista[0] != None:
            lista[0].append(f"TFIDF_{doc}")
        else:
            lista[0] = ["Termo", f"TFIDF_{doc}"]
        for termo in index_docs['index']:
            if lista[ind_t] == None:
                lista[ind_t] = [termo]
            if termo in index_docs['docs'][doc]['termos']:
                lista[ind_t].append(index_docs['docs'][doc]
                                    ['termos'][termo]['tfidf'])
            else:
                lista[ind_t].append(0)
            ind_t += 1
        ind_t = 1
    print(tabulate(lista[1:],
                headers=lista[0]))
