####
# Funciones para procesamiento del texto.
####

# Obtener el texto de todos los ficheros de un directorio
def obtainNews(path):
    import os
    dirs = os.listdir(path)
    list = []
    for file in dirs:
        bytes = os.path.getsize(path+file)
        fd = os.open(path+file, os.O_RDONLY)
        text = os.read(fd, bytes)
        os.close(fd)
        list.append(text)
    return list

# Operador de tokenización
def tokenizeList(list):
    from nltk.tokenize import TweetTokenizer
    tokensList = []
    for elemento in list:
        tmp= []
        tknzr = TweetTokenizer()
        tmp = tknzr.tokenize(elemento)
        tokensList.append(tmp)
    return tokensList

# Convierte a minusculas
def transformCases(list):
    lowerTokens = []
    for tokens in list:
        lowerList = []
        for element in tokens:
            lower = element.lower()
            lowerList.append(lower)
        lowerTokens.append(lowerList)
    return lowerTokens

# operador stop words
def stopWords(list):
    #import nltk
    #nltk.download('stopwords')
    from nltk.corpus import stopwords
    stop_words_sp = set(stopwords.words('spanish'))
    stopWordsList = []
    for words in list:
        filtered_sentence = []
        filtered_sentence = [w for w in words if w not in stop_words_sp]
        for w in words:
            if w not in stop_words_sp:
                filtered_sentence.append(w)
        stopWordsList.append(filtered_sentence)
    return stopWordsList

# operador de filtro por largo de palabra
def filterLength(list):
    result = []
    for element in list:
        elements = []
        for word in element:
            if (len(word) > 2):
                elements.append(word)
        result.append(elements)
    return result

# operador que elimina las URL's
def removeURLs(list):
    result = []
    for element in list:
        elements = []
        for word in element:
            if not word.startswith("https://"):
                elements.append(word)
        result.append(elements)
    return result

# operador de lematización
def stemList(list):
    from nltk.stem import SnowballStemmer
    spanish_stemmer = SnowballStemmer('spanish')
    stemmedList = []
    for element in list:
        stemmed = []
        for word in element:
            stemmed.append(spanish_stemmer.stem(word))
        stemmedList.append(stemmed)
    return stemmedList

# esto es solo para comprobar eliminar en la versión final
def doJob():
    # Use a breakpoint in the code line below to debug your script.
    path = "/home/rafa/Documents/" #variable de la caja de texto que ha hecho Carlos
    noticias = obtainNews(path)
    print(noticias)
    tokensList = tokenizeList(noticias)
    print(tokensList)
    lower = transformCases(tokensList)
    print(lower)
    stop = stopWords(lower)
    print(stop)
    filter = filterLength(stop)
    print(filter)
    sinURL = removeURLs(filter)
    print(sinURL)
    stemmed = stemList(sinURL)
    print(stemmed)

if __name__ == '__main__':
    doJob()
