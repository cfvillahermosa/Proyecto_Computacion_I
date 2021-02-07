from ventana_ui import *
from textproc import *
from algorithms import *
from nltk.corpus import stopwords
import pickle
import os
import re

import easygui
import nltk
##########################################
import numpy as np
from nltk.tokenize import word_tokenize
from sklearn.datasets import load_files
nltk.download('wordnet')

# import nltk

nltk.download('stopwords')


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    pathTrainNews = ''

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        # abrimos el explorador de archivos para las noticias de despoblación
        self.pushButton_abrir_despoblacion.clicked.connect(
            self.abrirNoticiasDespoblacion)

        # # abrimos el explorador de archivos para las noticias de no despoblación
        # self.pushButton_abrir_no_despoblacion.clicked.connect(
        #     self.abrirNoticasNoDespoblacion)

        # rellenamos el comboBox con las distintas opciones de algoritmos
        self.setAlgoritmos()

        # función ejecutar
        self.pushButton_ejecutar.clicked.connect(self.ejecutar)

        #funcion cargar modelo
        self.pushButton_abrir_no_despoblacion.clicked.connect(self.loadModel)

        

    # Esta función abre el explorador de archivos para seleccionar las noticias de despoblación
    # Además establece en el elemento lineEdit asociado la ruta seleccionada
    def abrirNoticiasDespoblacion(self):
        self.pathTrainNews = easygui.diropenbox()
        list = os.listdir(self.pathTrainNews)
        numeroNoticiasDespoblacion = len(list)
        print(numeroNoticiasDespoblacion)
        self.lineEdit_despoblacion.setText(self.pathTrainNews)

    # Esta función abre el explorador de archivos para seleccionar las noticias de no despoblación
    # Además establece en el elemento lineEdit asociado la ruta seleccionada
    def abrirNoticasNoDespoblacion(self):
        self.lineEdit_no_despoblacion.setText(easygui.diropenbox())

    def setAlgoritmos(self):
        self.comboBox.addItem('Decision tree')
        self.comboBox.addItem('Random forest')
        self.comboBox.addItem('SVM (Support Vector Machine)')

    def ejecutar(self):
        X,y = proccessText(self.pathTrainNews)

        selectedAlgorithm = self.comboBox.currentText()

        if selectedAlgorithm == 'Random forest':
            print('### random forest')
            randomForest(X,y)
            # plotter(X,y)
        elif selectedAlgorithm == 'Decision tree':
            print('### decision tree')
            decisionTree(X,y)
            # plotter(X,y)
        elif selectedAlgorithm == 'SVM (Support Vector Machine)':
            print('### SVM')
            supportVectorMachine(X,y)
            # plotter(X,y)

    def loadModel(self):
        self.pathModelNews = easygui.diropenbox()
        X,y = proccessText(self.pathModelNews)
        with open('decision_tree_text_classifier', 'rb') as training_model:
            model = pickle.load(training_model)

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

        y_pred2 = model.predict(X_test)
        from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
        print(confusion_matrix(y_test, y_pred2))
        print(classification_report(y_test, y_pred2))
        print(accuracy_score(y_test, y_pred2)) 

        ### grafico matplob
        # import matplotlib.pyplot as plt  
        # from sklearn.datasets import make_classification
        # from sklearn.metrics import plot_confusion_matrix
        # from sklearn.model_selection import train_test_split
        # from sklearn.svm import SVC
        # X, y = make_classification(random_state=0)
        # X_train, X_test, y_train, y_test = train_test_split(
        #         X, y, random_state=0)
        # clf = SVC(random_state=0)
        # clf.fit(X_train, y_train)

        # plot_confusion_matrix(clf, X_test, y_test)  
        # plt.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
