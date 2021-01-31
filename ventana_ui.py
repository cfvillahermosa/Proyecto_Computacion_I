# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(959, 685)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 20, 901, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_despoblacion = QtWidgets.QLabel(self.tab)
        self.label_despoblacion.setGeometry(QtCore.QRect(30, 50, 131, 16))
        self.label_despoblacion.setObjectName("label_despoblacion")
        self.label_no_despoblacion = QtWidgets.QLabel(self.tab)
        self.label_no_despoblacion.setGeometry(QtCore.QRect(30, 100, 141, 16))
        self.label_no_despoblacion.setObjectName("label_no_despoblacion")
        self.label_seleccionar_algoritmo = QtWidgets.QLabel(self.tab)
        self.label_seleccionar_algoritmo.setGeometry(QtCore.QRect(30, 170, 141, 16))
        self.label_seleccionar_algoritmo.setObjectName("label_seleccionar_algoritmo")
        self.lineEdit_despoblacion = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_despoblacion.setGeometry(QtCore.QRect(210, 50, 301, 20))
        self.lineEdit_despoblacion.setReadOnly(True)
        self.lineEdit_despoblacion.setObjectName("lineEdit_despoblacion")
        self.pushButton_abrir_despoblacion = QtWidgets.QPushButton(self.tab)
        self.pushButton_abrir_despoblacion.setGeometry(QtCore.QRect(560, 50, 75, 23))
        self.pushButton_abrir_despoblacion.setObjectName("pushButton_abrir_despoblacion")
        self.lineEdit_no_despoblacion = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_no_despoblacion.setGeometry(QtCore.QRect(210, 100, 301, 20))
        self.lineEdit_no_despoblacion.setReadOnly(True)
        self.lineEdit_no_despoblacion.setObjectName("lineEdit_no_despoblacion")
        self.pushButton_abrir_no_despoblacion = QtWidgets.QPushButton(self.tab)
        self.pushButton_abrir_no_despoblacion.setGeometry(QtCore.QRect(560, 100, 75, 23))
        self.pushButton_abrir_no_despoblacion.setObjectName("pushButton_abrir_no_despoblacion")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(210, 170, 301, 22))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.textBrowser_vista_previa = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_vista_previa.setGeometry(QtCore.QRect(30, 220, 471, 111))
        self.textBrowser_vista_previa.setObjectName("textBrowser_vista_previa")
        self.pushButton_ejecutar = QtWidgets.QPushButton(self.tab)
        self.pushButton_ejecutar.setGeometry(QtCore.QRect(560, 260, 111, 41))
        self.pushButton_ejecutar.setObjectName("pushButton_ejecutar")
        self.textBrowser_resultado = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_resultado.setGeometry(QtCore.QRect(30, 340, 821, 121))
        self.textBrowser_resultado.setObjectName("textBrowser_resultado")
        self.label_guardar_modelo = QtWidgets.QLabel(self.tab)
        self.label_guardar_modelo.setGeometry(QtCore.QRect(30, 490, 111, 16))
        self.label_guardar_modelo.setObjectName("label_guardar_modelo")
        self.lineEdit_guardar_modelo = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_guardar_modelo.setGeometry(QtCore.QRect(120, 490, 501, 20))
        self.lineEdit_guardar_modelo.setReadOnly(True)
        self.lineEdit_guardar_modelo.setObjectName("lineEdit_guardar_modelo")
        self.pushButton_guardar_modelo = QtWidgets.QPushButton(self.tab)
        self.pushButton_guardar_modelo.setGeometry(QtCore.QRect(650, 490, 75, 23))
        self.pushButton_guardar_modelo.setObjectName("pushButton_guardar_modelo")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_noticias_clasificar = QtWidgets.QLabel(self.tab_2)
        self.label_noticias_clasificar.setGeometry(QtCore.QRect(20, 30, 141, 16))
        self.label_noticias_clasificar.setObjectName("label_noticias_clasificar")
        self.label_modelo_clasificador = QtWidgets.QLabel(self.tab_2)
        self.label_modelo_clasificador.setGeometry(QtCore.QRect(20, 80, 111, 16))
        self.label_modelo_clasificador.setObjectName("label_modelo_clasificador")
        self.lineEdit_noticias_clasificar = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_noticias_clasificar.setGeometry(QtCore.QRect(160, 30, 401, 20))
        self.lineEdit_noticias_clasificar.setReadOnly(True)
        self.lineEdit_noticias_clasificar.setObjectName("lineEdit_noticias_clasificar")
        self.lineEdit_modelo_clasificador = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_modelo_clasificador.setGeometry(QtCore.QRect(160, 80, 401, 20))
        self.lineEdit_modelo_clasificador.setReadOnly(True)
        self.lineEdit_modelo_clasificador.setObjectName("lineEdit_modelo_clasificador")
        self.pushButton_noticias_clasificar = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_noticias_clasificar.setGeometry(QtCore.QRect(600, 30, 75, 23))
        self.pushButton_noticias_clasificar.setObjectName("pushButton_noticias_clasificar")
        self.pushButton_modelo_clasificador = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_modelo_clasificador.setGeometry(QtCore.QRect(600, 80, 75, 23))
        self.pushButton_modelo_clasificador.setObjectName("pushButton_modelo_clasificador")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(20, 140, 471, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.textBrowser_resumen = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_resumen.setGeometry(QtCore.QRect(510, 140, 331, 192))
        self.textBrowser_resumen.setObjectName("textBrowser_resumen")
        self.label_guardar_resultados = QtWidgets.QLabel(self.tab_2)
        self.label_guardar_resultados.setGeometry(QtCore.QRect(30, 380, 111, 16))
        self.label_guardar_resultados.setObjectName("label_guardar_resultados")
        self.lineEdit_guardar_resultados = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_guardar_resultados.setGeometry(QtCore.QRect(170, 380, 391, 20))
        self.lineEdit_guardar_resultados.setReadOnly(True)
        self.lineEdit_guardar_resultados.setObjectName("lineEdit_guardar_resultados")
        self.pushButton_guardar = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_guardar.setGeometry(QtCore.QRect(590, 380, 75, 23))
        self.pushButton_guardar.setObjectName("pushButton_guardar")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 959, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_despoblacion.setText(_translate("MainWindow", "Noticias de despoblación"))
        self.label_no_despoblacion.setText(_translate("MainWindow", "Noticias de no despoblación"))
        self.label_seleccionar_algoritmo.setText(_translate("MainWindow", "Seleccionar algoritmo:"))
        self.lineEdit_despoblacion.setText(_translate("MainWindow", "Ruta"))
        self.pushButton_abrir_despoblacion.setText(_translate("MainWindow", "Abrir"))
        self.lineEdit_no_despoblacion.setText(_translate("MainWindow", "Ruta"))
        self.pushButton_abrir_no_despoblacion.setText(_translate("MainWindow", "Abrir"))
        self.textBrowser_vista_previa.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">VISTA PREVIA:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Ejemplares &quot;despoblación&quot;:    XXX</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Ejemplares &quot;no despoblación&quot;:         XXX</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Total:        XXX</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Algoritmo seleccionado:    ---------------</p></body></html>"))
        self.pushButton_ejecutar.setText(_translate("MainWindow", "EJECUTAR"))
        self.textBrowser_resultado.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Resultado:</span></p></body></html>"))
        self.label_guardar_modelo.setText(_translate("MainWindow", "Guardar modelo:"))
        self.lineEdit_guardar_modelo.setText(_translate("MainWindow", "Ruta"))
        self.pushButton_guardar_modelo.setText(_translate("MainWindow", "Guardar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Entrenamiento"))
        self.label_noticias_clasificar.setText(_translate("MainWindow", "Noticias para clasificar: "))
        self.label_modelo_clasificador.setText(_translate("MainWindow", "Modelo clasificador:"))
        self.lineEdit_noticias_clasificar.setText(_translate("MainWindow", "Ruta"))
        self.lineEdit_modelo_clasificador.setText(_translate("MainWindow", "Ruta"))
        self.pushButton_noticias_clasificar.setText(_translate("MainWindow", "Seleccionar"))
        self.pushButton_modelo_clasificador.setText(_translate("MainWindow", "Seleccionar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Noticia"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Despoblación"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ver noticia"))
        self.textBrowser_resumen.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">RESUMEN:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">    </span>Total noticias:         XXX</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Despoblación:        XXX</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    No Despoblación:    XXX</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Tiempo: 17 seg.</p></body></html>"))
        self.label_guardar_resultados.setText(_translate("MainWindow", "Guardar resultados:"))
        self.lineEdit_guardar_resultados.setText(_translate("MainWindow", "Ruta"))
        self.pushButton_guardar.setText(_translate("MainWindow", "Guardar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Clasificación"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

