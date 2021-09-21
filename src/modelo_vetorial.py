import math


def tf_idf_documents(index_docs: dict):
    for doc in index_docs['docs']:
        freq_maxima = index_docs['docs'][doc]['max']
        soma = 0
        for termo in index_docs['docs'][doc]['termos']:
            index_docs['docs'][doc]['termos'][termo]['tfidf'] = (
                index_docs['docs'][doc]['termos'][termo]['freq']/freq_maxima)*index_docs['index'][termo]['idf']
            index_docs['docs'][doc]['termos'][termo]['quad'] = index_docs['docs'][doc]['termos'][termo]['tfidf']**2
            soma += index_docs['docs'][doc]['termos'][termo]['quad']
        index_docs['docs'][doc]['raiz'] = math.sqrt(soma)


def print_tf_idf(index_docs: dict):
    lenght_t = len(index_docs['index'])+1
    lista = [None]*lenght_t
    ind_t = 1
    for doc in index_docs['docs']:
        if lista[0] != None:
            lista[0].append(f"TFIDF_{doc}")
        else:
            lista[0] = [f"TFIDF_{doc}"]
        for termo in index_docs['index']:
            if lista[ind_t] == None:
                lista[ind_t] = []
            if termo in index_docs['docs'][doc]['termos']:
                lista[ind_t].append(index_docs['docs'][doc]
                                    ['termos'][termo]['tfidf'])
            else:
                lista[ind_t].append(0)
            ind_t += 1
        ind_t = 1
    for x in lista:
        print(x)
