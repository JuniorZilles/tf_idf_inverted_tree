from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk import download

from unidecode import unidecode

import re

def download_stop_words()->None:
    """
    Ação pré requisito da biblioteca
    baixar as stopwords
    """
    download('stopwords')
    download('punkt')

def remove_stop_words(text:str)->list:
    """
    Tranforma o texto para lower case, 
    substitu caracteres que não sejam números e letras, 
    remove stopwords e remove acentuação 
    
    args:
        text:str texto a ser processado
    returns:
        retorna uma lista ordenada de palavras
    """
    lower_text = text.lower()
    text_rep = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ ]', '', lower_text)
    stop_words_port = set(stopwords.words('portuguese')) 
    word_tokens = word_tokenize(text_rep) 
    filtered_sentence = [unidecode(w) for w in word_tokens if not w in stop_words_port] 
    return filtered_sentence
