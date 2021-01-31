import os

import easygui

from ventana_ui import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

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

    # Esta función abre el explorador de archivos para seleccionar las noticias de despoblación
    # Además establece en el elemento lineEdit asociado la ruta seleccionada
    def abrirNoticiasDespoblacion(self):
        ruta = easygui.diropenbox()
        list = os.listdir(ruta)
        numeroNoticiasDespoblacion = len(list)
        print(numeroNoticiasDespoblacion)
        self.lineEdit_despoblacion.setText(ruta)

    # Esta función abre el explorador de archivos para seleccionar las noticias de no despoblación
    # Además establece en el elemento lineEdit asociado la ruta seleccionada
    def abrirNoticasNoDespoblacion(self):
        self.lineEdit_no_despoblacion.setText(easygui.diropenbox())

    def setAlgoritmos(self):
        self.comboBox.addItem('Árbol de decisión')
        self.comboBox.addItem('Bayes')


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
