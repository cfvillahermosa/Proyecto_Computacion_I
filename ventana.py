import os
import easygui
from ventana_ui import *
from textproc import *
import nltk

from nltk.tokenize import word_tokenize


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    ruta_despoblacion = ''

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        # abrimos el explorador de archivos para las noticias de despoblación
        self.pushButton_abrir_despoblacion.clicked.connect(
            self.abrirNoticiasDespoblacion)

        # abrimos el explorador de archivos para las noticias de no despoblación
        self.pushButton_abrir_no_despoblacion.clicked.connect(
            self.abrirNoticasNoDespoblacion)

        # rellenamos el comboBox con las distintas opciones de algoritmos
        self.setAlgoritmos()

        # función ejecutar
        self.pushButton_ejecutar.clicked.connect(self.ejecutar)

    # Esta función abre el explorador de archivos para seleccionar las noticias de despoblación
    # Además establece en el elemento lineEdit asociado la ruta seleccionada
    def abrirNoticiasDespoblacion(self):
        self.ruta_despoblacion = easygui.diropenbox()
        list = os.listdir(self.ruta_despoblacion)
        numeroNoticiasDespoblacion = len(list)
        print(numeroNoticiasDespoblacion)
        self.lineEdit_despoblacion.setText(self.ruta_despoblacion)

    # Esta función abre el explorador de archivos para seleccionar las noticias de no despoblación
    # Además establece en el elemento lineEdit asociado la ruta seleccionada
    def abrirNoticasNoDespoblacion(self):
        self.lineEdit_no_despoblacion.setText(easygui.diropenbox())

    def setAlgoritmos(self):
        self.comboBox.addItem('Árbol de decisión')
        self.comboBox.addItem('Bayes')

    def ejecutar(self):
        list = obtainNews(self.ruta_despoblacion+'/')
        tokenizedList = tokenizeList(list)
        transformedCaseList = transformCases(tokenizedList)
        stoppedWordsList = stopWords(transformedCaseList)
        filteredListByLength = filterLength(stoppedWordsList)
        deletedUrlsList = removeURLs(filteredListByLength)
        # nltk.download('punkt')
        stemmedList = stemList(deletedUrlsList)
        classifier = nltk.NaiveBayesClassifier.train(stemmedList)
        # print(stemmedList)
        # train = [('I love this sandwich.', 'pos'),
        #          ('This is an amazing place!', 'pos'),
        #          ('I feel very good about these beers.', 'pos'),
        #          ('This is my best work.', 'pos'),
        #          ("What an awesome view", 'pos'),
        #          ('I do not like this restaurant', 'neg'),
        #          ('I am tired of this stuff.', 'neg'),
        #          ("I can't deal with this", 'neg'),
        #          ('He is my sworn enemy!', 'neg'),
        #          ('My boss is horrible.', 'neg')]
        # all_words = set(word.lower()
        #                 for passage in train for word in word_tokenize(passage[0]))
        # t = [({word: (word in word_tokenize(x[0]))
        #        for word in all_words}, x[1]) for x in train]
        # print(t)
        print(classifier)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


[({'deal': False, 'these': False, 'he': False, 'an': False, 'awesome': False, 'best': False, 'tired': False, 'about': False, 'sworn': False, 'is': False, '.': True, 'horrible': False, 'i': False, 'am': False, 'like': False, 'ca': False, 'my': False, 'view': False, 'amazing': False, 'of': False, 'sandwich': True, 'with': False, 'very': False, 'feel': False, 'work': False, 'not': False, 'boss': False, 'what': False, 'love': True, 'stuff': False, '!': False, 'this': True, "n't": False, 'good': False, 'enemy': False, 'beers': False, 'place': False, 'restaurant': False, 'do': False}, 'pos'), ({'deal': False, 'these': False, 'he': False, 'an': True, 'awesome': False, 'best': False, 'tired': False, 'about': False, 'sworn': False, 'is': True, '.': False, 'horrible': False, 'i': False, 'am': False, 'like': False, 'ca': False, 'my': False, 'view': False, 'amazing': True, 'of': False, 'sandwich': False, 'with': False, 'very': False, 'feel': False, 'work': False, 'not': False, 'boss': False, 'what': False, 'love': False, 'stuff': False, '!': True, 'this': False, "n't": False, 'good': False, 'enemy': False, 'beers': False, 'place': True, 'restaurant': False, 'do': False}, 'pos'), ({'deal': False, 'these': True, 'he': False, 'an': False, 'awesome': False, 'best': False, 'tired': False, 'about': True, 'sworn': False, 'is': False, '.': True, 'horrible': False, 'i': False, 'am': False, 'like': False, 'ca': False, 'my': False, 'view': False, 'amazing': False, 'of': False, 'sandwich': False, 'with': False, 'very': True, 'feel': True, 'work': False, 'not': False, 'boss': False, 'what': False, 'love': False, 'stuff': False, '!': False, 'this': False, "n't": False, 'good': True, 'enemy': False, 'beers': True, 'place': False, 'restaurant': False, 'do': False}, 'pos'), ({'deal': False, 'these': False, 'he': False, 'an': False, 'awesome': False, 'best': True, 'tired': False, 'about': False, 'sworn': False, 'is': True, '.': True, 'horrible': False, 'i': False, 'am': False, 'like': False, 'ca': False, 'my': True, 'view': False, 'amazing': False, 'of': False, 'sandwich': False, 'with': False, 'very': False, 'feel': False, 'work': True, 'not': False, 'boss': False, 'what': False, 'love': False, 'stuff': False, '!': False, 'this': False, "n't": False, 'good': False, 'enemy': False, 'beers': False, 'place': False, 'restaurant': False, 'do': False}, 'pos'), ({'deal': False, 'these': False, 'he': False, 'an': True, 'awesome': True, 'best': False, 'tired': False, 'about': False, 'sworn': False, 'is': False, '.': False, 'horrible': False, 'i': False, 'am': False, 'like': False, 'ca': False, 'my': False, 'view': True, 'amazing': False, 'of': False, 'sandwich': False, 'with': False, 'very': False, 'feel': False, 'work': False, 'not': False, 'boss': False, 'what': False, 'love': False, 'stuff': False, '!': False, 'this': False, "n't": False, 'good': False, 'enemy': False, 'beers': False, 'place': False, 'restaurant': False, 'do': False}, 'pos'),
 ({'deal': False, 'these': False, 'he': False, 'an': False, 'awesome': False, 'best': False, 'tired': False, 'about': False, 'sworn': False, 'is': False, '.': False, 'horrible': False, 'i': False, 'am': False, 'like': True, 'ca': False, 'my': False, 'view': False, 'amazing': False, 'of': False, 'sandwich': False, 'with': False, 'very': False, 'feel': False, 'work': False, 'not': True, 'boss': False, 'what': False, 'love': False, 'stuff': False, '!': False, 'this': True, "n't": False, 'good': False, 'enemy': False, 'beers': False, 'place': False, 'restaurant': True, 'do': True}, 'neg'), ({'deal': False, 'these': False, 'he': False, 'an': False, 'awesome': False, 'best': False, 'tired': True, 'about': False, 'sworn': False, 'is': False, '.': True, 'horrible': False, 'i': False, 'am': True, 'like': False, 'ca': False, 'my': False, 'view': False, 'amazing': False, 'of': True, 'sandwich': False, 'with': False, 'very': False, 'feel': False, 'work': False, 'not': False, 'boss': False, 'what': False, 'love': False, 'stuff': True, '!': False, 'this': True, "n't": False, 'good': False, 'enemy': False, 'beers': False, 'place': False, 'restaurant': False, 'do': False}, 'neg'), ({'deal': True, 'these': False, 'he': False, 'an': False, 'awesome': False, 'best': False, 'tired': False, 'about': False, 'sworn': False, 'is': False, '.': False, 'horrible': False, 'i': False, 'am': False, 'like': False, 'ca': True, 'my': False, 'view': False, 'amazing': False, 'of': False, 'sandwich': False, 'with': True, 'very': False, 'feel': False, 'work': False, 'not': False, 'boss': False, 'what': False, 'love': False, 'stuff': False, '!': False, 'this': True, "n't": True, 'good': False, 'enemy': False, 'beers': False, 'place': False, 'restaurant': False, 'do': False}, 'neg'), ({'deal': False, 'these': False, 'he': False, 'an': False, 'awesome': False, 'best': False, 'tired': False, 'about': False, 'sworn': True, 'is': True, '.': False, 'horrible': False, 'i': False, 'am': False, 'like': False, 'ca': False, 'my': True, 'view': False, 'amazing': False, 'of': False, 'sandwich': False, 'with': False, 'very': False, 'feel': False, 'work': False, 'not': False, 'boss': False, 'what': False, 'love': False, 'stuff': False, '!': True, 'this': False, "n't": False, 'good': False, 'enemy': True, 'beers': False, 'place': False, 'restaurant': False, 'do': False}, 'neg'), ({'deal': False, 'these': False, 'he': False, 'an': False, 'awesome': False, 'best': False, 'tired': False, 'about': False, 'sworn': False, 'is': True, '.': True, 'horrible': True, 'i': False, 'am': False, 'like': False, 'ca': False, 'my': False, 'view': False, 'amazing': False, 'of': False, 'sandwich': False, 'with': False, 'very': False, 'feel': False, 'work': False, 'not': False, 'boss': True, 'what': False, 'love': False, 'stuff': False, '!': False, 'this': False, "n't": False, 'good': False, 'enemy': False, 'beers': False, 'place': False, 'restaurant': False, 'do': False}, 'neg')]
