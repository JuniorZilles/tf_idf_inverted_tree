import logging
from src.read_files import get_files_path
from src.pre_process import download_stop_words
from src.index import index_files, print_index
from src.modelo_vetorial import tf_idf_documents, print_tf_idf


def main():
    logging.info("Carregando arquivos")
    files = get_files_path()

    logging.info("Download Stopwords")
    download_stop_words()
    
    logging.info("Indexando arquivos")
    indexed = index_files(files)

    show_ind = int(input("Show inverted index: 0 - no; 1 - yes\n"))
    if show_ind == 1:
        print_index(indexed['index'])

    tf_idf_documents(indexed)

    show_tf = int(input("Show vector model: 0 - no; 1 - yes\n"))
    if show_tf == 1:
        print_tf_idf(indexed)



main()