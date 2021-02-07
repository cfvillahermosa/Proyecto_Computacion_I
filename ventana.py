import os
import pickle
import re

import easygui
import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.datasets import load_files

from algorithms import *
from textproc import *
from ventana_ui import *
from PyQt5 import QtCore, QtWidgets, QtGui
nltk.download('wordnet')
from PyQt5.QtWidgets import QTableWidgetItem

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

        # rellenamos el comboBox con los modelos
        self.setModels()

        # función ejecutar
        self.pushButton_ejecutar.clicked.connect(self.ejecutar)

        # funcion cargar modelo
        self.pushButton_modelo_clasificador.clicked.connect(self.loadModel)

        self.comboBox.currentTextChanged.connect(self.changeComboOption)

        self.comboBox_modelos.currentTextChanged.connect(self.changeComboModelOption)


    # Esta función abre el explorador de archivos para seleccionar las noticias de despoblación
    # Además establece en el elemento lineEdit asociado la ruta seleccionada

    def changeComboOption(self):
        self.textBrowser_resultado.setText('Resultado:')
    
    def changeComboModelOption(self):
        self.label_score.setText('Score:')
        self.tableWidget.setRowCount(0)

    def abrirNoticiasDespoblacion(self):
        self.pathTrainNews = easygui.diropenbox()
        list = os.listdir(self.pathTrainNews)
        numeroNoticiasDespoblacion = len(list)
        print(numeroNoticiasDespoblacion)
        self.lineEdit_despoblacion.setText(self.pathTrainNews)

    def abrirNoticiasClasificar(self):
        self.pathTrainNews = easygui.diropenbox()
        list = os.listdir(self.pathTrainNews)
        numeroNoticiasDespoblacion = len(list)
        print(numeroNoticiasDespoblacion)
        self.lineEdit_despoblacion.setText(self.pathTrainNews)

    def setAlgoritmos(self):
        self.comboBox.addItem('Decision tree')
        self.comboBox.addItem('Random forest')
        self.comboBox.addItem('SVM (Support Vector Machine)')

    def setModels(self):
        self.comboBox_modelos.addItem('Decision tree')
        self.comboBox_modelos.addItem('Random forest')
        self.comboBox_modelos.addItem('SVM (Support Vector Machine)')

    def ejecutar(self):
        X, y, fileNames, targetNames = proccessText(self.pathTrainNews)

        selectedAlgorithm = self.comboBox.currentText()

        if selectedAlgorithm == 'Random forest':
            randomForest(X, y, self)
        elif selectedAlgorithm == 'Decision tree':
            decisionTree(X, y, self)
        elif selectedAlgorithm == 'SVM (Support Vector Machine)':
            supportVectorMachine(X, y, self)

    def loadModel(self):
        self.pathModelNews = easygui.diropenbox()
        self.lineEdit_noticias_clasificar.setText(self.pathModelNews)
        X, y, filenames, targetNames = proccessText(self.pathModelNews)
        selectedModel = self.comboBox_modelos.currentText()
        if selectedModel == 'Random forest':
            model = pickle.load(open('random_forest_text_classifier', 'rb'))
        elif selectedModel == 'Decision tree':
            model = pickle.load(open('decision_tree_text_classifier', 'rb'))
        elif selectedModel == 'SVM (Support Vector Machine)':
            model = pickle.load(open('svm_text_classifier', 'rb'))

        prediction = model.predict(X)
        fileNamesArr = []
        labelsArr = ['Despoblación','No despoblación']
        tableIndex = 0;
        for i in filenames:
            completeFilename = i
            i = i.replace(self.pathModelNews, '')
            i = i.replace(targetNames[0], '')
            i = i.replace('\\', '')
            fileNamesArr.append(i)
            self.tableWidget.insertRow(tableIndex)
            itemFileName = QTableWidgetItem(str(i))
            itemLabel = QTableWidgetItem(labelsArr[prediction[tableIndex]])
            itemViewNew = QTableWidgetItem(completeFilename)
            self.tableWidget.setItem(tableIndex,0,itemFileName)
            self.tableWidget.setItem(tableIndex,1,itemLabel)
            self.tableWidget.setItem(tableIndex,2,itemViewNew)
            tableIndex = tableIndex +1

        
            

        result = model.score(X, y)
        self.label_score.setText("Score: {0:.2f} %".format(100 * result))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
