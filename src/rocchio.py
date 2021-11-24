from src.measures import get_relevant_documents


def get_tfidf_docs_list(indexed: dict, relevant_docs):
    lista_centroide_rel = {}
    lista_centroide_ire = {}

    for doc in list(indexed['docs'].keys()):
        for termo in indexed['docs'][doc]['termos']:
            if doc in relevant_docs:
                if termo not in lista_centroide_rel:
                    lista_centroide_rel[termo] = indexed['docs'][doc]['termos'][termo]['tfidf']
                else:
                    lista_centroide_rel[termo] += indexed['docs'][doc]['termos'][termo]['tfidf']
                if termo not in lista_centroide_ire:
                    lista_centroide_ire[termo] = 0
            else:
                if termo not in lista_centroide_rel:
                    lista_centroide_rel[termo] = 0
                if termo not in lista_centroide_ire:
                    lista_centroide_ire[termo] = indexed['docs'][doc]['termos'][termo]['tfidf']
                else:
                    lista_centroide_ire[termo] += indexed['docs'][doc]['termos'][termo]['tfidf']

    return lista_centroide_rel,  lista_centroide_ire


def get_query_list(indexed: dict, query: str):
    query = query.split(' ')
    lista_query = {}
    for doc in list(indexed['docs'].keys()):
        for termo in indexed['docs'][doc]['termos']:
            if termo in query:
                if termo not in lista_query:
                    lista_query[termo] = indexed['docs'][doc]['termos'][termo]['tfidf']
                else:
                    lista_query[termo] += indexed['docs'][doc]['termos'][termo]['tfidf']
            else:
                lista_query[termo] = 0
    return lista_query


def execute_rocchio(indexed: dict, relevants: str, query: str, alpha=0.8, beta=0.4, gamma=0.1):
    documents = list(indexed['docs'].keys())
    relevant_list = relevants.split(',')
    relevants_list = get_relevant_documents(documents, relevant_list)
    lista_centroide_rel, lista_centroide_ire = get_tfidf_docs_list(
        indexed, relevants_list)
    lista_query = get_query_list(indexed, query)
    lista_rocchio = {}
    qtd_rel = len(relevant_list)
    qtd_ire = len(documents) - qtd_rel
    for i in list(lista_query.keys()):
        part1 = alpha*lista_query[i]
        part2 = (beta*lista_centroide_rel[i])/qtd_rel
        part3 = (gamma*lista_centroide_ire[i])/qtd_ire
        if part1 + part2 - part3 <= 0:
            lista_rocchio[i]={'valor':0, 'rel': part2, 'ire': part3}
        else:
             lista_rocchio[i]={'valor':part1 + part2 - part3, 'rel': part2, 'ire': part3}
    print_rocchio(lista_rocchio)
    return lista_rocchio


def print_rocchio(lista_rocchio):
    for i in list(lista_rocchio.keys()):
        print(f'Termo: {i}')
        print(f'Relevantes: {lista_rocchio[i]["rel"]}')
        print(f'Irrelevantes: {lista_rocchio[i]["ire"]}')

def extract_terms(lista_rocchio:list):
    lista_termos = []
    for i in list(lista_rocchio.keys()):
        if lista_rocchio[i]['valor'] != 0:
            lista_termos.append(i)
    return ' '.join(lista_termos)