import traceback
from src.read_files import get_files_path
from src.pre_process import download_stop_words
from src.index import index_files, print_index
from src.tf_idf import tf_idf_documents, print_tf_idf
from src.search import calculate_similarity, print_similaritys
from src.measures import calculate_measures, print_documents, print_measure
from src.plot import plot_graphics


def main():
    try:
        print("Loading files")
        files = get_files_path()

        print("Downloading stopwords")
        download_stop_words()
        
        print("Indexing files")
        indexed = index_files(files)

        show_ind = int(input("Show inverted index: 0 - no; 1 - yes\n"))
        if show_ind == 1:
            print_index(indexed['index'])

        print("Computing vector model")
        tf_idf_documents(indexed)

        show_tf = int(input("Show vector model: 0 - no; 1 - yes\n"))
        if show_tf == 1:
            print_tf_idf(indexed)

        run = 1
        while run != 0:
            consulta = str(input("Search:\n"))
            
            print("Computing similarity ...")
            similaritys = calculate_similarity(indexed, consulta)

            print_similaritys(similaritys)

            print_documents(indexed)

            relevants = str(input("Which documents are relevant (split each using ',', eg. 1,3,5):"))

            print("Computing measures ...")
            measure = calculate_measures(relevants, similaritys, indexed)

            print_measure(measure)


            print("Plotting graphics ...")
            plot_graphics(measure)

            run = int(input("Do another search: 0 - no; 1 - yes\n"))
    except Exception as e:
        traceback.print_exc()
main()