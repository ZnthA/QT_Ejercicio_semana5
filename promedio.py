import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "promedio.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Aqui van los botones
        self.btnCalcular.clicked.connect(self.fn_calculo)

    #Aqui van las funciones
    def fn_calculo(self):
    	n1 = float(self.txtN1.text())
    	n2 = float(self.txtN2.text())
    	n3 = float(self.txtN3.text())
    	prom = round((n1+n2+n3)/3,2)
    	self.txtProm.setText(str(prom))
    	if prom >= 12.5:
    		self.txtCalif.setText("Aprobado")
    	else:
    		self.txtCalif.setText("Desaprobado")


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())