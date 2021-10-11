from tabulate import tabulate


def calculate_measures(relevants: str, retrieved: dict, indexed: dict) -> dict:
    """
    Calcula as medidas de avaliação e monta a lista de recall e precision
    args:
        relevants:str -> lista das posições dos documentos relevantes dentro da lista de documentos
            1,2,3,4
        retrieved:dict -> documentos recuperados na consulta
            {'documento1':'similaridade', 'documento2': 'similaridade'} 
        indexed:dict -> indice
            {"index": {"termo1":{'df': 1, 'idf': 0, 'docs': {'arquivo.txt': 1}}}, "docs": {'termos':{'termo1':{'freq':1}}}}
    returns:
        {
            "precion": precision, "recall": recall, 
            "f_measure": f_measure, "avg_prec": avg_prec, 
            "recall_list": recall_list, "precision_list": precision_list
        }
    """
    documents = list(indexed['docs'].keys())
    relevant_list = relevants.split(',')
    retrived_list = list(retrieved.keys())
    relevants = get_relevant_documents(documents, relevant_list)

    rec_total = len(retrived_list)
    rel_total = len(relevants)

    recall_list = [0]
    precision_list = [1.0]

    precision = 0
    recall = 0
    f = 0
    avg_prec = 0

    prec_rel = []
    relevant = False
    rec_rel = 0
    count = 1
    for a in range(0, rec_total):
        if retrived_list[a] in relevants:
            rec_rel += 1
            relevant = True

        c_recall = recall_measure(count, rec_rel)
        c_precision = precision_measure(count, rec_rel)
        recall_list.append(c_recall)
        precision_list.append(c_precision)

        if relevant:
            prec_rel.append(c_precision)
            relevant = False
        count += 1

    precision = precision_measure(rec_total, rec_rel)
    recall = recall_measure(rel_total, rec_rel)
    f = f_measure(precision, recall)
    avg_prec = avg_precision(prec_rel)

    return {
        "precision": precision, "recall": recall, 
        "f_measure": f, "avg_prec": avg_prec, 
        "recall_list": recall_list, "precision_list": precision_list
    }


def avg_precision(precions: list) -> float:
    return sum(precions)/len(precions)


def recall_measure(rel: int, rel_rec: int) -> float:
    return rel_rec / rel


def precision_measure(rec: int, rel_rec: int) -> float:
    return rel_rec / rec


def f_measure(precision: float, recall: float) -> float:
    return 2*((precision*recall)/(precision+recall))


def get_relevant_documents(documents: list, relevants: list) -> list:
    """
    Obtem os nomes dos documentos relevantes
    args:
        documents:list -> nome dos documentos 
            ["doc1", "doc2", ...]
        relevants:list -> indices dos documentos relevantes
            [1,2,3]
    return:
        list with the names of relevant documents
    """
    rel = []
    for r in relevants:
        i = int(r)
        if documents[i] not in rel:
            rel.append(documents[i])
    return rel

def print_documents(indexed: dict) -> None:
    """
    Mostra os documentos disponíveis no indice
    args:
        indexed:dict 
            {"index": {"termo1":{'df': 1, 'idf': 0, 'docs': {'arquivo.txt': 1}}}, "docs": {'termos':{'termo1':{'freq':1}}}}
    """
    documents = list(indexed['docs'].keys())
    print("Existing documents:")
    print(tabulate([documents], headers=[x for x in range(0, len(documents))]))


def print_measure(measures:dict)-> None:
    print(f"precision: {measures['precision']}")
    print(f"recall: {measures['recall']}") 
    print(f"f_measure: {measures['f_measure']}") 
    print(f"avgPrecision: {measures['avg_prec']}") 
            